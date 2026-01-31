import pandas as pd
from pathlib import Path

STAGING_PATH = Path("data/staging")
CLEAN_PATH = Path("data/staging_clean")

def clean_customers():
    df = pd.read_csv(STAGING_PATH / "customers_staging.csv")

    # primary key check
    if df["customer_id"].isnull().any():
        raise ValueError("customer_id NULL ditemukan")

    if df["customer_id"].duplicated().any():
        raise ValueError("customer_id DUPLICATE ditemukan")

    CLEAN_PATH.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_PATH / "customers_clean.csv", index=False)

    print(f"[CLEAN CUSTOMERS] rows: {len(df)}")

if __name__ == "__main__":
    clean_customers()