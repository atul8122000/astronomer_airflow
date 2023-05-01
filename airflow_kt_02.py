# Import airflow package
from airflow import DAG
from datetime import timedelta

# default arguments - Common attributes of your task
default_args = {
    "owner": "airflow",
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "admin@localhost.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# Defining DAG with no task and default arguments

## with CRON EXPRESSION
with DAG('airflow_kt_dag_02',
 default_args=default_args,
 schedule_interval='*/10 * * * *',
 catchup=False):
 None



## with TIMEDELTA OBJECT
with DAG('airflow_kt_dag_02',
 default_args=default_args,
 schedule_interval=timedelta(minutes=10),
 catchup=False):
 None