CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE warehouse.dim_customer (
    customer_id VARCHAR PRIMARY KEY,
    customer_unique_id VARCHAR,
    customer_city VARCHAR,
    customer_state VARCHAR
);

CREATE TABLE warehouse.dim_date (
    date DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT,
    day_of_week VARCHAR
);

CREATE TABLE warehouse.dim_order_status (
    order_status VARCHAR PRIMARY KEY
);

CREATE TABLE warehouse.fact_orders (
    order_id VARCHAR PRIMARY KEY,
    customer_id VARCHAR,
    order_status VARCHAR,
    order_purchase_timestamp TIMESTAMP,

    FOREIGN KEY (customer_id) REFERENCES warehouse.dim_customer(customer_id),
    FOREIGN KEY (order_status) REFERENCES warehouse.dim_order_status(order_status)
);