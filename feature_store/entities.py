from feast import Entity
from feast.value_type import ValueType

ticker = Entity(
    name="ticker",
    join_keys=["ticker"],
    value_type=ValueType.STRING,
)
