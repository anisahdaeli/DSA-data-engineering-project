import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

WAREHOUSE_PATH = Path("data/warehouse")

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/ecommerce_dw"
)

def truncate_table(table_name):
    with engine.begin() as conn:
        conn.execute(
            text(f"TRUNCATE TABLE warehouse.{table_name} CASCADE;")
        )
    print(f"[TRUNCATE] {table_name}")

def load_table(csv_name, table_name):
    df = pd.read_csv(WAREHOUSE_PATH / csv_name)
    df.to_sql(
        table_name,
        engine,
        schema="warehouse",
        if_exists="append",
        index=False
    )
    print(f"[LOAD] {table_name} rows: {len(df)}")

if __name__ == "__main__":

    # DIMENSIONS FIRST
    truncate_table("fact_orders")
    truncate_table("dim_customer")
    truncate_table("dim_date")
    truncate_table("dim_order_status")

    load_table("dim_customer.csv", "dim_customer")
    load_table("dim_date.csv", "dim_date")
    load_table("dim_order_status.csv", "dim_order_status")

    # FACT LAST
    load_table("fact_orders.csv", "fact_orders")
