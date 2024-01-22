from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
default_args = {
    'owner': 'sugumar',
    'start_date': datetime(2024, 1, 4),
    'retries': 1,
}
dag = DAG(
    'task4',
    default_args=default_args,
    schedule_interval='*/4 * * * *',
    catchup=False
)
query = """
    INSERT INTO Purchase_details (customer_id, total_orders, total_returns, created_time)
    SELECT
        o.customer_id,
        COUNT(o.order_id) AS total_orders,
        COUNT(pr.return_id) AS total_returns,
        NOW() AS created_time
    FROM Orders o
    LEFT JOIN Product_returns pr ON o.customer_id = pr.customer_id
    GROUP BY o.customer_id;
"""
calculate_purchase = PostgresOperator(
    task_id="calculate_purchase_details",
    postgres_conn_id="airflow-postgres",
    sql=query,
    dag=dag,
)

calculate_purchase