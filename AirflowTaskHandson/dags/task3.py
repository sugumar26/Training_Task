from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'sugumar',
    'start_date': datetime(2024, 1, 4),
    'retries': 1,
}

dag = DAG(
    'task3',
    default_args=default_args,
    schedule_interval='*/2 * * * *',
    catchup=False
)

query1 = """
    INSERT INTO Orders (customer_id, order_date)
    VALUES 
        ( 1, NOW() - INTERVAL '1 minute'),
        ( 2, NOW() - INTERVAL '1 minute')
"""



query2 = """
    INSERT INTO Product_returns (customer_id, return_date)
    VALUES 
    ( 1, NOW() - INTERVAL '1 minute'),
    ( 2, NOW() - INTERVAL '1 minute')
"""


orderstable = PostgresOperator(
    task_id="insert_into_orders",
    postgres_conn_id="airflow-postgres",
    sql=query1,
    dag=dag,
)

producttable = PostgresOperator(
    task_id="insert_into_product_returns",
    postgres_conn_id="airflow-postgres",
    sql=query2,
    dag=dag,
)

orderstable >> producttable
