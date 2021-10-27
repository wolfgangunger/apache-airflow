from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from random import randint
from airflow.operators.bash import BashOperator



with DAG(
    "my_dag2", 
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

    b1 >> b2

