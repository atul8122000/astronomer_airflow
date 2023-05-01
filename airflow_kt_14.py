from airflow import DAG
import datetime
from airflow.operators.mysql_operator import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2020-02-28'}

with DAG('airflow_kt_dag_14',
 schedule_interval='*/5 * * * *', 
 start_date=datetime(2018, 11, 1),
 catchup=False):
    
    
    mysql_task = MySqlOperator(
            mysql_conn_id='mysql_default', 
            task_id='mysql_task',
            sql='<path>/sample_sql.sql'
            # params={'test_user_id': -99}
    )

mysql_task