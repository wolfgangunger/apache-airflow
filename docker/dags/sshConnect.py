import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
from airflow.contrib.operators.ssh_operator import SSHOperator

args = {
    "owner": "airflow",
    "provide_context": True,
}
with DAG(
    dag_id="remote_server_direct_key02", 
    schedule_interval='@daily', 
    start_date=days_ago(2), 
    tags=['unw', 'test'],  
    default_args=args, 
    catchup=False
    ) as dag:
    task1 = BashOperator(
        task_id="pem_script00",
        bash_command="/usr/local/airflow/.local/bin/aws secretsmanager get-secret-value --secret-id your-key-name --query 'SecretString' --output text |base64 -d > /tmp/your-key-name.pem"
   )

    task2 = SSHOperator(
        task_id="ssh_script00",
        ssh_conn_id='ssh_new',
        command='aws s3 cp s3://<bucket-name>/bashtest/scripts/ssh_connection.sh . && cat ssh_connection.sh | bash - ',
   )

task1 >> task2