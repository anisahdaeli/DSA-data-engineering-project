import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
STAGING_PATH = Path("data/staging")

def extract_orders():
    file_path = RAW_PATH / "olist_orders_dataset.csv"

    if not file_path.exists():
        raise FileNotFoundError("File orders tidak ditemukan")

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Data orders kosong")

    STAGING_PATH.mkdir(parents=True, exist_ok=True)
    output_path = STAGING_PATH / "orders_staging.csv"
    df.to_csv(output_path, index=False)

    print(f"[EXTRACT ORDERS] rows: {len(df)} → saved to staging")

if __name__ == "__main__":
    extract_orders()