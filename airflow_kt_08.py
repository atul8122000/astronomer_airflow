from airflow import DAG
from pendulum import datetime
from airflow.models.baseoperator import chain
from airflow.operators.empty import EmptyOperator


with DAG('airflow_kt_dag_08',
 schedule_interval='*/5 * * * *', 
 start_date=datetime(2018, 11, 1),
 catchup=False):

 # create multiple task in function with empty operator
 def dependencies():
    t0 = EmptyOperator(task_id="t0")
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")
    t3 = EmptyOperator(task_id="t3")
    t4 = EmptyOperator(task_id="t4")
    t5 = EmptyOperator(task_id="t5")
    t6 = EmptyOperator(task_id="t6")

# task dependencies using chain funtion
    chain(t0, t1, [t2, t3], [t4, t5], t6)


dependencies()