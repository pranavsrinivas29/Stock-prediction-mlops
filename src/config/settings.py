from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Raw data
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "stocks"

# Feature data
FEATURE_DATA_DIR = PROJECT_ROOT / "data" / "features" / "stocks"

# Ensure dirs exist
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
FEATURE_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Supported tickers (single source of truth)
TICKERS = ["AAPL"]
