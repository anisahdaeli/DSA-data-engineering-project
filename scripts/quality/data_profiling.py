import pandas as pd

# load data
orders = pd.read_csv("data/olist_orders_dataset.csv")
customers = pd.read_csv("data/olist_customers_dataset.csv")

print("ORDERS")
print(orders.info())
print("\nCUSTOMERS")
print(customers.info())