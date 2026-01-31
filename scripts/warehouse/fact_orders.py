import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/staging_clean")
WAREHOUSE_PATH = Path("data/warehouse")

def build_fact_orders():
    orders = pd.read_csv(CLEAN_PATH / "orders_clean.csv")

    fact_orders = orders[[
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp"
    ]]

    WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)
    fact_orders.to_csv(WAREHOUSE_PATH / "fact_orders.csv", index=False)

    print(f"[FACT ORDERS] rows: {len(fact_orders)}")

if __name__ == "__main__":
    build_fact_orders()
