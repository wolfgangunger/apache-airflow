#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance

from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import ShortCircuitOperator

with DAG(
    dag_id='short_circuit_operator',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['unw', 'test'],
) as dag:
    cond_true = ShortCircuitOperator(
        task_id='condition_is_True',
        python_callable=lambda: True,
    )

    cond_false = ShortCircuitOperator(
        task_id='condition_is_False',
        python_callable=lambda: False,
    )

    ds_true = [DummyOperator(task_id='true_' + str(i)) for i in [1, 2]]
    ds_false = [DummyOperator(task_id='false_' + str(i)) for i in [1, 2, 3]]

    chain(cond_true, *ds_true)
    chain(cond_false, *ds_false)