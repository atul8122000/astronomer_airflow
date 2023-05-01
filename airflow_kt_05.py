from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator



with DAG(dag_id='airflow_kt_dag_05',
 schedule_interval=None, 
 start_date=datetime(2020, 1, 1), 
 catchup=False) as dag:

# Note: firstly you have to create postgres connection from airflow UI
# Task --> create table using PostgresOperator
   create_country_table = PostgresOperator(
      task_id="create_country_table",
      postgres_conn_id="country_postgres",
      sql="""
         CREATE TABLE IF NOT EXISTS random (
               country VARCHAR NOT NULL,
               country_code VARCHAR NOT NULL
         );
         """
   )