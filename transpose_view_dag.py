from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['your@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'transpose_view_dag',
    default_args=default_args,
    description='Crea la vista transpuesta en PostgreSQL',
    # Programa la ejecución 3 veces al día a las 00:00, 08:00 y 16:00
    schedule_interval='0 0,8,16 * * *',
)

create_transpose_view = PythonOperator(
    task_id='create_transpose_view',
    python_callable=transpose_view,
    dag=dag,
)

create_transpose_view
