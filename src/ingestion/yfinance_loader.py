import yfinance as yf
import pandas as pd
from datetime import datetime
from src.config.settings import RAW_DATA_DIR


def load_stock_data(
    ticker: str,
    start: str,
    end: str,
    interval: str = "1d"
) -> pd.DataFrame:
    """
    Load raw OHLCV stock data from yfinance.
    """
    df = yf.download(
        tickers=ticker,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data fetched for ticker {ticker}")

    df.reset_index(inplace=True)
    df["ticker"] = ticker
    df["ingestion_timestamp"] = datetime.utcnow()

    return df


def save_raw_data(df: pd.DataFrame, ticker: str) -> None:
    """
    Save raw data as parquet (immutable raw layer).
    """
    output_path = RAW_DATA_DIR / f"{ticker}.parquet"
    df.to_parquet(output_path, index=False)
    print(f"✅ Saved raw data → {output_path}")


if __name__ == "__main__":
    df = load_stock_data(
        ticker="AAPL",
        start="2018-01-01",
        end="2025-01-01"
    )
    save_raw_data(df, "AAPL")
