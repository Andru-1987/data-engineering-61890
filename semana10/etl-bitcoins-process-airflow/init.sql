-- DROP DATABASE IF EXISTS etl_bitcoins;

-- CREATE DATABASE etl_bitcoins;

-- -- Connect to the database manually if needed in a script that is not run at init
-- --\c etl_bitcoins;

CREATE SCHEMA etl_bitcoins_schema;

CREATE TABLE etl_bitcoins_schema.mining_data (
    mining_algo VARCHAR(200),
    network_hash_rate VARCHAR(200),
    available_on_nicehash_percent FLOAT,
    one_hour_attack_cost FLOAT,
    twenty_four_hours_attack_cost FLOAT,
    attack_appeal FLOAT,
    hash_rate FLOAT,
    hash_rate_30d_average FLOAT,
    mining_revenue_per_hash_usd FLOAT,
    mining_revenue_per_hash_native_units FLOAT,
    mining_revenue_per_hash_per_second_usd FLOAT,
    mining_revenue_per_hash_per_second_native_units FLOAT,
    mining_revenue_from_fees_percent_last_24_hours FLOAT,
    mining_revenue_native FLOAT,
    mining_revenue_usd FLOAT,
    mining_revenue_total FLOAT,
    average_difficulty FLOAT,
    date TIMESTAMP
);
