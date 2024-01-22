from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
default_args = {
    'owner': 'sugumar',
    'start_date': datetime(2024, 1, 4),
    'retries': 1,
}
dag = DAG(
    'task2',
    default_args=default_args,
    schedule_interval=None,
)
def add(a, b):
    result = a + b
    print(f"Addition Result: {result}")

def subtract(c, d):
    result = c - d
    print(f"Subtraction Result: {result}")

def multiply(e, f):
    result = e * f
    print(f"Multiplication Result: {result}")

a, b, c, d, e, f = 10, 5, 10, 5, 4, 6

addition = PythonOperator(
    task_id='addition_task',
    python_callable=add,
    op_kwargs={'a': a, 'b': b},
    dag=dag,
)    
subtraction=PythonOperator(
    task_id='subraction',
    python_callable=subtract,
    op_kwargs={'c':c,'d':d},
    dag=dag,
)
Multiplication=PythonOperator(
    task_id='multiplication',
    python_callable=multiply,
    op_kwargs={'e':e,'f':f},
    dag=dag,
)

# addition>>subtraction>>Multiplication
[addition,subtraction,Multiplication]