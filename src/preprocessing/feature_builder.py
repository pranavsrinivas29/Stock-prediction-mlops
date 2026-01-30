# src/preprocessing/feature_builder.py
import numpy as np
import pandas as pd
from src.preprocessing.cleaner import clean_raw_stock_df


def add_price_features(df):
    df = df.copy()
    df["return"] = df["Close"].pct_change()
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    return df


def add_lag_features(df, lags=(1, 3)):
    df = df.copy()
    for lag in lags:
        df[f"return_lag_{lag}"] = df["log_return"].shift(lag)
        df[f"close_lag_{lag}"] = df["Close"].shift(lag)
    return df


def add_rolling_features(df, windows=(2, 3)):
    df = df.copy()
    for w in windows:
        df[f"rolling_mean_{w}"] = df["log_return"].rolling(w).mean()
        df[f"rolling_std_{w}"] = df["log_return"].rolling(w).std()
    return df


def add_moving_averages(df, windows=(3, 10)):
    df = df.copy()
    for w in windows:
        df[f"sma_{w}"] = df["Close"].rolling(w).mean()
        df[f"ema_{w}"] = df["Close"].ewm(span=w, adjust=False).mean()
    return df


def add_volume_features(df, window=10):
    df = df.copy()
    df["volume_change"] = df["Volume"].pct_change()
    df[f"volume_rolling_mean_{window}"] = df["Volume"].rolling(window).mean()
    return df


def add_time_features(df):
    df = df.copy()
    df["day_of_week"] = df.index.dayofweek
    df["week_of_year"] = df.index.isocalendar().week.astype(int)
    df["month"] = df.index.month
    df["is_month_end"] = df.index.is_month_end.astype(int)
    return df


def build_feature_table(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_raw_stock_df(df)

    df = add_price_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    df = add_moving_averages(df)
    df = add_volume_features(df)
    df = add_time_features(df)

    df = df.drop(columns=["Open", "High", "Low", "Volume"], errors="ignore")
    df = df.dropna()

    return df
