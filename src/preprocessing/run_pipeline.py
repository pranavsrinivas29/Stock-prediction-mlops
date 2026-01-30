import pandas as pd
from src.preprocessing.feature_builder import build_feature_table
from src.config.settings import RAW_DATA_DIR, FEATURE_DATA_DIR, TICKERS


def run_for_ticker(ticker: str):
    raw_path = RAW_DATA_DIR / f"{ticker}.parquet"
    feature_path = FEATURE_DATA_DIR / f"{ticker}_features.parquet"

    df_raw = pd.read_parquet(raw_path)
    df_features = build_feature_table(df_raw)
    df_features.to_parquet(feature_path)

    print(f"✅ Features saved for {ticker} → {feature_path}")


def main():
    for ticker in TICKERS:
        run_for_ticker(ticker)


if __name__ == "__main__":
    main()
