from feast import FileSource

stock_features_source = FileSource(
    name="stock_features_source",
    path="../data/features/stocks/*.parquet",
    timestamp_field="Date",
)
