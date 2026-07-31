WITH item_totals AS (
    SELECT
        item_type,
        COUNT(*) AS items_per_batch,
        SUM(square_footage) AS batch_square_footage
    FROM Inventory
    GROUP BY item_type
),
prime_allocation AS (
    SELECT
        items_per_batch,
        batch_square_footage,
        FLOOR(500000 / batch_square_footage) AS batch_count
    FROM item_totals
    WHERE item_type = 'prime_eligible'
),
allocation AS (
    SELECT
        'prime_eligible' AS item_type,
        batch_count * items_per_batch AS item_count,
        0 AS type_priority
    FROM prime_allocation
    UNION ALL
    SELECT
        'not_prime' AS item_type,
        FLOOR(
            (500000 - prime.batch_count * prime.batch_square_footage)
            / non_prime.batch_square_footage
        ) * non_prime.items_per_batch AS item_count,
        1 AS type_priority
    FROM prime_allocation AS prime
    CROSS JOIN item_totals AS non_prime
    WHERE non_prime.item_type = 'not_prime'
)
SELECT item_type, item_count
FROM allocation
ORDER BY item_count DESC, type_priority ASC;
