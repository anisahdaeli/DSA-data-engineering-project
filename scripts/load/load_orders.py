import pandas as pd
from config.database import get_engine

engine = get_engine()

fact_orders = pd.read_csv("data/processed/fact_orders.csv")

fact_orders.to_sql(
    "fact_orders",
    engine,
    if_exists="append",
    index=False
)

print("FACT ORDERS LOADED")