from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

import sys

sys.path.append("/opt/airflow/project")

from producer.generate_orders import generate_orders


with DAG(
    dag_id="first_pipeline",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    tags=["learning", "project2"],
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    generate_orders_task = PythonOperator(
        task_id="generate_orders",
        python_callable=generate_orders,
        op_kwargs={
            "num_orders": 10
        }
    )

    finish = EmptyOperator(
        task_id="finish"
    )

    start >> generate_orders_task >> finish