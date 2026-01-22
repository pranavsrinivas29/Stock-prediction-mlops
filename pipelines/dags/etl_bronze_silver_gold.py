from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# -----------------------------
# Default DAG arguments
# -----------------------------
default_args = {
    "owner": "mlops",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# -----------------------------
# DAG definition
# -----------------------------
with DAG(
    dag_id="etl_bronze_silver_gold",
    description="Bronze → Silver → Gold ETL pipeline",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "finance", "mlops"],
) as dag:

    bronze_ingest = BashOperator(
        task_id="bronze_ingestion",
        bash_command="python -m etl.bronze.ingest_prices",
    )

    silver_clean = BashOperator(
        task_id="silver_clean_validate",
        bash_command="python -m etl.silver.clean_validate",
    )

    gold_features = BashOperator(
        task_id="gold_feature_engineering",
        bash_command="python -m etl.gold.build_features",
    )

    # Task dependencies
    bronze_ingest >> silver_clean >> gold_features
