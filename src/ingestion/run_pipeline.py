from src.ingestion.yfinance_loader import load_stock_data, save_raw_data

def run_ingestion_pipeline(
    ticker: str,
    start: str,
    end: str
):
    df = load_stock_data(
        ticker=ticker,
        start=start,
        end=end
    )
    save_raw_data(df, ticker)
