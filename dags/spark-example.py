from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_jdbc import SparkJDBCOperator
from airflow.providers.apache.spark.operators.spark_sql import SparkSqlOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
	'start_date': datetime(2023,4,1)
}

with DAG(dag_id='spark-example'
		,schedule_interval='@daily'
		,default_args=default_args
		,tags=['spark']
		,catchup=False) as dag:

	sql_job = SparkSqlOperator(sql="select 1+1",master = 'local', task_id = 'sql_job')
