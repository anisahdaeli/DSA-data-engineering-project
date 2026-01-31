import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/staging_clean")
WAREHOUSE_PATH = Path("data/warehouse")

def build_dim_order_status():
    df = pd.read_csv(CLEAN_PATH / "orders_clean.csv")

    dim_status = pd.DataFrame({
        "order_status": df["order_status"].unique()
    })

    WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)
    dim_status.to_csv(WAREHOUSE_PATH / "dim_order_status.csv", index=False)

    print(f"[DIM STATUS] rows: {len(dim_status)}")

if __name__ == "__main__":
    build_dim_order_status()
