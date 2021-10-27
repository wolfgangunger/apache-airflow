from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from random import randint
from airflow.operators.bash import BashOperator

def _method1():
    return randint(1,10)

with DAG(
    "my_dag3", 
    start_date=datetime(2021,1,1),
    schedule_interval="@daily",
    tags=['unw', 'test'],
    catchup=False
    ) as dag:


    
    b1 = BashOperator(
        task_id="b1",
        bash_command="echo '################## b1'"     
    )
    
    b2 = BashOperator(
        task_id="b2",
        bash_command="echo '################## b2'"     
    )

    p1 = PythonOperator(
        task_id="p1",
        python_callable=_method1
    )


    b1 >> b2 >> p1

