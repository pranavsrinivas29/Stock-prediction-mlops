from feast import FeatureView, Field
from feast.types import Float32, Int64

from entities import ticker
from data_sources import stock_features_source


stock_features_view = FeatureView(
    name="stock_features",
    entities=[ticker],
    ttl=None,
    schema=[
        # Price & return features
        Field(name="Close", dtype=Float32),
        Field(name="return", dtype=Float32),
        Field(name="log_return", dtype=Float32),

        # Lag features
        Field(name="return_lag_1", dtype=Float32),
        Field(name="Close_lag_1", dtype=Float32),
        Field(name="return_lag_3", dtype=Float32),
        Field(name="Close_lag_3", dtype=Float32),

        # Rolling statistics
        Field(name="rolling_mean_2", dtype=Float32),
        Field(name="rolling_std_2", dtype=Float32),
        Field(name="rolling_mean_3", dtype=Float32),
        Field(name="rolling_std_3", dtype=Float32),

        # Moving averages
        Field(name="sma_3", dtype=Float32),
        Field(name="ema_3", dtype=Float32),
        Field(name="sma_10", dtype=Float32),
        Field(name="ema_10", dtype=Float32),

        # Volume features
        Field(name="volume_change", dtype=Float32),
        Field(name="volume_rolling_mean_10", dtype=Float32),

        # Time features
        Field(name="day_of_week", dtype=Int64),
        Field(name="week_of_year", dtype=Int64),
        Field(name="month", dtype=Int64),
        Field(name="is_month_end", dtype=Int64),
    ],
    source=stock_features_source,
)
