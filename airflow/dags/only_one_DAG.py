import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import psycopg2 as db

from elasticsearch import Elasticsearch, helpers

import pandas as pd
import json
import os

def fetch_data():
    conn_string="dbname='airflow' host='postgres' port='5432' user='airflow' password='airflow'" # container to container hostname and port
    conn=db.connect(conn_string)
    df=pd.read_sql("select * from table_m3", conn)
    df.to_csv('/opt/airflow/dags/raw_data.csv', index=False)
    print("Data extracted and saved to raw_data.csv")

def clean_data():
    df = pd.read_csv('/opt/airflow/dags/raw_data.csv')
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.lower()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.to_csv('/opt/airflow/dags/data_cleaned.csv', index=False)
    print("Data cleaned and saved to csv")

def load_data_to_elasticsearch():
    es = Elasticsearch('http://elasticsearch:9200')
    es.indices.create(index='connectpostgres', ignore=400)
    df = pd.read_csv('/opt/airflow/dags/data_cleaned.csv')
    json_data = df.to_json(orient='records', lines=True)
    actions = []
    for line in json_data.splitlines():
        try:
            # Convert each line of JSON to a dictionary
            source = json.loads(line)
            actions.append({
                "_op_type": "index",  # Operation type: index
                "_index": "connectpostgres",  # Elasticsearch index name
                "_source": source  # The actual document data
            })
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON line: {e}")
            continue  # Skip the invalid line

    # Perform the bulk indexing
    try:
        success, failed = helpers.bulk(es, actions, chunk_size=500)
        print(f"Successfully indexed {success} documents.")
        if failed:
            print(f"Failed to index {len(failed)} documents.")
            for error in failed:
                print(error)
    except ElasticsearchException as e:
        print(f"Elasticsearch error: {e}")
    except Exception as e:
        print(f"General error during bulk indexing: {e}")


default_args = {
    'owner': 'nathaniel',
    'start_date': dt.datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG(
    'insert_only_one',
    default_args=default_args,
    schedule_interval=None  # Set schedule_interval to None to run the DAG only once

) as dag:
    
    extract_task = PythonOperator(
        task_id='fetch',
        python_callable=fetch_data,
        provide_context=True,
    )
    clean_task = PythonOperator(
        task_id='clean',
        python_callable=clean_data,
        provide_context=True,
    )
    load_task = PythonOperator(
        task_id='load',
        python_callable=load_data_to_elasticsearch,
        provide_context=True,
    )

# Set task dependencies
extract_task >> clean_task >> load_task