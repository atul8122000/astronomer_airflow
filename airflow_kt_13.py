from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#push
def _extract(ti):
    partner_name = "netflix"
    ti.xcom_push(key="partner_name", value=partner_name)
#pull
def _process(ti):
    partner_name = ti.xcom_pull(key="partner_name", task_ids="extract")
    print(partner_name)

with DAG(dag_id='airflow_kt_dag_13',
 schedule_interval=None, 
 start_date=datetime(2020, 1, 1), 
 catchup=False) as dag:
    
        python_task_1	= PythonOperator(
          task_id='python_task',
          python_callable= _extract          )
        
        python_task_2	= PythonOperator(
          task_id='python_task',
          python_callable= _process
          )

python_task_1 >> python_task_2