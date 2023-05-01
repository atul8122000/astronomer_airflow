from airflow import DAG
from pendulum import datetime
from airflow.utils.task_group import TaskGroup
from airflow.operators.empty import EmptyOperator

with DAG('airflow_kt_dag_09',
 schedule_interval='*/5 * * * *', 
 start_date=datetime(2018, 11, 1),
 catchup=False):
 
 t0 = EmptyOperator(task_id="start")

# Start Task Group definition
with TaskGroup(group_id="group1") as tg1:
    t1 = EmptyOperator(task_id="task1")
    t2 = EmptyOperator(task_id="task2")

    t1 >> t2

# End Task Group definition
t3 = EmptyOperator(task_id="end")

# Set Task Group's (tg1) dependencies
t0 >> tg1 >> t3