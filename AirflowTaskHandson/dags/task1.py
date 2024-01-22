from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

default_args = {
    'owner': 'sugumar',
    'start_date': datetime(2024, 1, 4),
    'retries': 1,
}
dag = DAG(
    'task1',
    default_args=default_args,
    schedule_interval=None,
)
def create_airflow_variable(input_list):
    for word in input_list:
        Variable.set(word, word)
    print(f"Airflow variables created with input: {input_list}")
def find_word_lengths(input_list):
    word_lengths = {word: len(word) for word in input_list}
    print("Word lengths:", word_lengths)
task_create_variable = PythonOperator(
    task_id='create_airflow_variable',
    python_callable=create_airflow_variable,
    op_kwargs={'input_list': ["DAG", "variable", "preset"]},
    dag=dag,
)
task_find_word_lengths = PythonOperator(
    task_id='find_word_lengths',
    python_callable=find_word_lengths,
    op_kwargs={'input_list': ["DAG", "variable", "preset"]},
    dag=dag,
)
task_create_variable >> task_find_word_lengths
