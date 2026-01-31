import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/staging_clean")
WAREHOUSE_PATH = Path("data/warehouse")

def build_dim_customer():
    df = pd.read_csv(CLEAN_PATH / "customers_clean.csv")

    dim_customer = df[[
        "customer_id",
        "customer_unique_id",
        "customer_city",
        "customer_state"
    ]].drop_duplicates()

    WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)
    dim_customer.to_csv(WAREHOUSE_PATH / "dim_customer.csv", index=False)

    print(f"[DIM CUSTOMER] rows: {len(dim_customer)}")

if __name__ == "__main__":
    build_dim_customer()