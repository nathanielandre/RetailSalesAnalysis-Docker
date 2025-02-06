# Retail Supply Chain Sales Analysis
### This project involved analyzing historical sales data for a retail company to optimize supply chain operations and improve sales performance. Using Docker, Apache Airflow, PostgreSQL, Elasticsearch, and Kibana, I automated the data pipeline and visualized key business insights. The analysis focused on customer segmentation, sales trends, product performance, regional sales, and top customers, providing actionable insights for marketing, inventory management, and strategic decision-making.

[View the presentation as PDF](RetailSalesAnalysis.pdf)

## Dataset Source
```
Dataset is taken from :

Retail Supply Chain Sales Dataset
By SHANDEEP RAULA

```
<a href="https://www.kaggle.com/datasets/shandeep777/retail-supply-chain-sales-dataset">DATASET LINK</a>

## Role
Data analyst at a retail company 

## Background
You are a data analyst working for a retail company that operates in multiple regions and offers a diverse range of products. The company wants to optimize its supply chain operations, enhance customer targeting, and improve sales performance. You have been provided with a dataset containing historical sales data, which includes detailed information about customer orders, products, sales, and regions.

Your task is to analyze the sales and supply chain data to identify key patterns, trends, and actionable insights that could help the company make informed decisions regarding marketing, inventory management, and regional sales strategies.

## Goal
In general
- Analyzing retail sales performance and profitability.
- Identifying customer trends and product preferences.
- Studying the impact of geographic and temporal factors on sales.

## User
- Sales and Marketing Teams: To optimize campaigns and target high-value customers effectively.
- Logistics and Supply Chain Teams: To make informed decisions about inventory management, regional demand, and resource allocation.
- Senior Management: To monitor overall business performance and strategic decisions related to sales, product offerings, and market expansion.

## Architecture and Tools
```
This project leverages a modern stack of tools to automate the data pipeline and provide interactive insights:

Docker: Used to containerize all necessary components (Airflow, PostgreSQL, Elasticsearch, Kibana) for easy deployment and scalability.
Apache Airflow: Orchestrates the data pipeline, ensuring that tasks such as data extraction, transformation, and loading (ETL) are executed automatically.
PostgreSQL: Serves as the relational database for storing cleaned and processed sales data.
Elasticsearch: Indexed the processed sales data for fast search and analysis.
Kibana: Used for creating interactive visualizations and dashboards to explore the sales data.
```

## Data Pipeline
```
The data pipeline is designed to automate the ingestion, processing, and analysis of sales data:
1. Data Cleaning & Transformation: Raw sales data is cleaned and transformed using Python scripts, including handling missing values, date parsing, and normalization.
2. Loading Data into PostgreSQL: Cleaned data is loaded into a PostgreSQL database, which serves as the data warehouse for the analysis.
3. Indexing with Elasticsearch: The transformed data is indexed into Elasticsearch to provide fast search and querying capabilities.
4. Visualizations in Kibana: Interactive dashboards in Kibana display key insights, such as regional sales performance, product trends, customer segments, and top customers.

** Visualization can be seen in Kibana Insights folder
```

## Installation Instructions
To set up this project locally, follow these steps:

1. Clone this repository:
2. Install Docker if you haven't already.
3. Build and start the Docker environment:
```
docker-compose -f .\airflow\airflow.yaml up -d
```
The following services will be started:

- Airflow (for orchestrating the pipeline)
- PostgreSQL (for storing cleaned data)
- Elasticsearch (for indexing data)
- Kibana (for visualizing the data)

Access the services:
- Airflow UI: http://localhost:8080
- Kibana UI: http://localhost:5601

Once the pipeline is running, it will automatically extract, clean, process, and load the data into PostgreSQL and Elasticsearch. You can then explore the data in Kibana.