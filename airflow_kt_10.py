from airflow  import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable 

#Set variables in key value pair or in a json format
def _extract():
	Partner = Variable.get("airflow_kt_dag_10", deserialize_json=True)
	print(Partner)

with DAG('airflow_kt_dag_03',
 schedule_interval='*/5 * * * *', 
 start_date=datetime(2018, 11, 1),
 catchup=False):

# Task --> use python operator to run python function
    python_task	= PythonOperator(
          task_id='python_task',
          python_callable=_extract)