
"""
This is an example dag for ECSOperator.
The task "hello_world" runs `hello-world` task in `c` cluster.
It overrides the command in the `hello-world-container` container.
"""

import datetime
import os

from airflow import DAG
from airflow.providers.amazon.aws.operators.ecs import ECSOperator

dag = DAG(
    dag_id="unw_fargate",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
    },
    #default_view="graph",
    schedule_interval=None,
    start_date=datetime.datetime(2020, 1, 1),
    tags=['unw', 'test'],
)
# generate dag documentation
dag.doc_md = __doc__

# [START howto_operator_ecs]
hello_world = ECSOperator(
    task_id="hello_world",
    dag=dag,
    aws_conn_id="aws_ecs",
    region_name="eu-central-1",
    cluster="cluster-unw",
    task_definition="hello-world",
    launch_type="FARGATE",
    overrides={
        "containerOverrides": [
            {
                "name": "hello-world-container",
                "command": ["echo", "hello", "world"],
            },
        ],
    },
    network_configuration={
        "awsvpcConfiguration": {
            "securityGroups": [os.environ.get("SECURITY_GROUP_ID", "sg-123abc")],
            "subnets": [os.environ.get("SUBNET_ID", "subnet-123456ab")],
        },
    },
    tags={
        "Customer": "unw",
        "Project": "Test",
        "Application": "Simple Fargates",
        "Version": "0.0.1",
        "Environment": "Development",
    },
    awslogs_group="/ecs/hello-world",
    awslogs_stream_prefix="prefix_b/hello-world-container",  # prefix with container name
)
# [END howto_operator_ecs]