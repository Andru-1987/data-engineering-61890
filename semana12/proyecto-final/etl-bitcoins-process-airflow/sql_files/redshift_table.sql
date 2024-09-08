DROP TABLE IF EXISTS andru_ocatorres_coderhouse.mining_data ;

CREATE TABLE andru_ocatorres_coderhouse.mining_data (
    mining_algo VARCHAR(200),
    network_hash_rate VARCHAR(200),
    available_on_nicehash_percent NUMERIC,
    one_hour_attack_cost NUMERIC,
    twenty_four_hours_attack_cost NUMERIC,
    attack_appeal NUMERIC,
    hash_rate NUMERIC,
    hash_rate_30d_average NUMERIC,
    mining_revenue_per_hash_usd NUMERIC,
    mining_revenue_per_hash_native_units NUMERIC,
    mining_revenue_per_hash_per_second_usd NUMERIC,
    mining_revenue_per_hash_per_second_native_units NUMERIC,
    mining_revenue_from_fees_percent_last_24_hours NUMERIC,
    mining_revenue_native NUMERIC,
    mining_revenue_usd NUMERIC,
    mining_revenue_total NUMERIC,
    average_difficulty NUMERIC,
    date TIMESTAMP
);
