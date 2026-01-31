import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
STAGING_PATH = Path("data/staging")

def extract_customers():
    file_path = RAW_PATH / "olist_customers_dataset.csv"

    if not file_path.exists():
        raise FileNotFoundError("File customers tidak ditemukan")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Data customers kosong")

    STAGING_PATH.mkdir(parents=True, exist_ok=True)
    output_path = STAGING_PATH / "customers_staging.csv"
    df.to_csv(output_path, index=False)

    print(f"[EXTRACT CUSTOMERS] rows: {len(df)} → saved to staging")

if __name__ == "__main__":
    extract_customers()