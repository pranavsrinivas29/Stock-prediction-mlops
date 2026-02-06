from prefect import flow, task, get_run_logger
from datetime import datetime, timedelta

from src.ingestion.run_pipeline import run_ingestion_pipeline
from src.preprocessing.run_pipeline import run_for_ticker
from src.config.settings import TICKERS


@task(
    name="Ingest stock data",
    retries=1,
    retry_delay_seconds=30,
)
def ingest_task(ticker: str, start: str, end: str):
    run_ingestion_pipeline(ticker, start, end)


@task(
    name="Build features",
    retries=1,
    retry_delay_seconds=30,
)
def preprocess_task(ticker: str):
    run_for_ticker(ticker=ticker)


@flow(name="stock-mlops-data-pipeline")
def stock_pipeline(
    lookback_days: int = 365,
):  
    logger = get_run_logger()
    end = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    start = (datetime.today() - timedelta(days=lookback_days)).strftime("%Y-%m-%d")

    logger.info(f"Running pipeline from {start} to {end}")

    ingest_futures = []
    
    for ticker in TICKERS:
        ingest_future = ingest_task.submit(ticker, start, end)
        ingest_futures.append((ticker, ingest_future))

    # 🔑 WAIT explicitly and then preprocess
    for ticker, ingest_future in ingest_futures:
        ingest_future.result()          
        preprocess_task.submit(ticker).result() 


if __name__ == "__main__":
    stock_pipeline()
