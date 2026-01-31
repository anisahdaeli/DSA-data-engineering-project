import pandas as pd
from pathlib import Path

CLEAN_PATH = Path("data/staging_clean")
WAREHOUSE_PATH = Path("data/warehouse")

def build_dim_date():
    df = pd.read_csv(CLEAN_PATH / "orders_clean.csv")

    # Ambil DATE saja (tanpa jam)
    dates = pd.to_datetime(df["order_purchase_timestamp"]).dt.date.unique()

    date_df = pd.DataFrame({"date": dates})

    date_df["year"] = pd.to_datetime(date_df["date"]).dt.year
    date_df["month"] = pd.to_datetime(date_df["date"]).dt.month
    date_df["day"] = pd.to_datetime(date_df["date"]).dt.day
    date_df["day_of_week"] = pd.to_datetime(date_df["date"]).dt.day_name()

    WAREHOUSE_PATH.mkdir(parents=True, exist_ok=True)
    date_df.to_csv(WAREHOUSE_PATH / "dim_date.csv", index=False)

    print(f"[DIM DATE] rows: {len(date_df)}")

if __name__ == "__main__":
    build_dim_date()
