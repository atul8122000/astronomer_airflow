from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG(dag_id='airflow_kt_dag_04',
 schedule_interval=None, 
 start_date=datetime(2020, 1, 1), 
 catchup=False) as dag:

# Task --> use Bash Operator to run bash command
 bash_task = BashOperator(
    task_id='bash_task',
    bash_command="echo 'command executed from BashOperator'")
