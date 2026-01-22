from sqlalchemy import text
from etl.common.db import engine

STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS bronze_price_raw (
        ticker TEXT NOT NULL,
        date TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER,
        ingested_at TEXT,
        PRIMARY KEY (ticker, date)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS silver_price_clean (
        ticker TEXT NOT NULL,
        date TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER,
        PRIMARY KEY (ticker, date)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS gold_price_features (
        ticker TEXT NOT NULL,
        date TEXT NOT NULL,

        return REAL,
        log_return REAL,

        return_lag_1 REAL,
        return_lag_3 REAL,
        close_lag_1 REAL,
        close_lag_3 REAL,

        rolling_mean_1 REAL,
        rolling_mean_3 REAL,
        rolling_std_1 REAL,
        rolling_std_3 REAL,

        sma_3 REAL,
        sma_10 REAL,
        ema_3 REAL,
        ema_10 REAL,

        volume_change REAL,
        volume_rolling_mean_10 REAL,

        day_of_week INTEGER,
        week_of_year INTEGER,
        month INTEGER,
        is_month_end INTEGER,

        PRIMARY KEY (ticker, date)
    );
    """
]

with engine.begin() as conn:
    for stmt in STATEMENTS:
        conn.execute(text(stmt))

print("✅ SQLite Bronze / Silver / Gold tables created successfully")
