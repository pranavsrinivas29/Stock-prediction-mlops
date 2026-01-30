# src/preprocessing/cleaner.py
import pandas as pd


def clean_raw_stock_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date")

    # Sort for time-series correctness
    df = df.sort_index()

    return df
