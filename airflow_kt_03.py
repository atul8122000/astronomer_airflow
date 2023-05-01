from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# python function
def my_func():
    print('Hello from my_func')

with DAG('airflow_kt_dag_03',
 schedule_interval='*/5 * * * *', 
 start_date=datetime(2018, 11, 1),
 catchup=False):

# Task --> use python operator to run python function
    python_task	= PythonOperator(task_id='python_task', python_callable=my_func)
