# src/preprocessing/cleaner.py
import pandas as pd


def clean_raw_stock_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    #print(df.columns)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").sort_index()

    return df
