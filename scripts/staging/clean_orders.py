import pandas as pd
from pathlib import Path

STAGING_PATH = Path("data/staging")
CLEAN_PATH = Path("data/staging_clean")

def clean_orders():
    df = pd.read_csv(STAGING_PATH / "orders_staging.csv")

    # convert datetime
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # primary key check
    if df["order_id"].isnull().any():
        raise ValueError("order_id NULL ditemukan")

    if df["order_id"].duplicated().any():
        raise ValueError("order_id DUPLICATE ditemukan")

    CLEAN_PATH.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_PATH / "orders_clean.csv", index=False)

    print(f"[CLEAN ORDERS] rows: {len(df)}")

if __name__ == "__main__":
    clean_orders()