-- Write your PostgreSQL query statement below
WITH summary AS (
    SELECT
        item_type,
        COUNT(*) AS item_count,
        SUM(square_footage) AS total_sqft
    FROM Inventory
    GROUP BY item_type
),
prime_calc AS (
    SELECT
        COALESCE(MAX(item_count), 0) AS prime_item_count,
        COALESCE(MAX(total_sqft), 0) AS prime_total_sqft,
        CASE
            WHEN COALESCE(MAX(total_sqft), 0) = 0 THEN 0
            ELSE FLOOR(500000 / MAX(total_sqft))
        END AS prime_batches
    FROM summary
    WHERE item_type = 'prime_eligible'
),
prime_result AS (
    SELECT
        'prime_eligible' AS item_type,
        (prime_batches * prime_item_count)::bigint AS item_count,
        (500000 - prime_batches * prime_total_sqft)::bigint AS remaining_sqft
    FROM prime_calc
),
not_prime_result AS (
    SELECT
        'not_prime' AS item_type,
        CASE
            WHEN s.total_sqft IS NULL OR s.total_sqft = 0 THEN 0
            ELSE (FLOOR(pr.remaining_sqft / s.total_sqft) * s.item_count)::bigint
        END AS item_count
    FROM prime_result pr
    LEFT JOIN summary s ON s.item_type = 'not_prime'
)
SELECT item_type, item_count FROM prime_result
UNION ALL
SELECT item_type, item_count FROM not_prime_result;

