import pandas as pd

# Load data
orders = pd.read_csv("data/olist_orders_dataset.csv")

# Convert timestamp columns to datetime
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

print(orders.info())

# Load customers
customers = pd.read_csv("data/olist_customers_dataset.csv")

# Join orders + customers
orders_customers = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

print(orders_customers.info())

# Create dim_customer
dim_customer = customers[[
    "customer_id",
    "customer_unique_id",
    "customer_city",
    "customer_state"
]].drop_duplicates()

print("DIM CUSTOMER")
print(dim_customer.info())

fact_orders = orders[[
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp"
]]

print("FACT ORDERS")
print(fact_orders.info())