from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# python function
def my_func():
    print('Hello from my_func')

with DAG('airflow_kt_dag_06',
 schedule_interval='*/5 * * * *', 
 start_date=datetime(2018, 11, 1),
 catchup=False):

# Multiple Task --> use python operator to run python function

    first_task = PythonOperator(
            task_id="first_task",
            python_callable=my_func
    )

    second_task = PythonOperator(
        task_id="second_task",
        python_callable=my_func
    )

    third_task = PythonOperator(
        task_id="third_task",
        python_callable=my_func
    )

    fourth_task = PythonOperator(
        task_id="fourth_task",
        python_callable=my_func
    )


# Task dependencies using bitshift operators (<< and >>)
first_task >> second_task >> third_task >> fourth_task