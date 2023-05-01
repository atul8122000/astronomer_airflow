# Import DAG from airflow package
from airflow import DAG

# Defining DAG with no task and minimum parameter
with DAG('airflow_kt_dag_01'):
    None