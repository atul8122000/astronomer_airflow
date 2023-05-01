from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG(dag_id='airflow_kt_dag_12',
 schedule_interval=None, 
 start_date=datetime(2020, 1, 1), 
 catchup=False) as dag:
    
    
    t1 = BashOperator(
    task_id="t1",
    bash_command='echo "{{ ti.xcom_push(key="k1", value="v1") }}" "{{ti.xcom_push(key="k2", value="v2") }}"',
    dag=dag,
    )

    t2 = BashOperator(
    task_id="t2",
    bash_command='echo "{{ ti.xcom_pull(key="k1") }}" "{{ ti.xcom_pull(key="k2") }}"',
    dag=dag,
    )
t1 >> t2