WITH RECURSIVE chains AS (
    SELECT
        giver_id AS start_id,
        receiver_id AS current_id,
        gift_value AS total_gift_value,
        1 AS chain_length
    FROM SecretSanta

    UNION ALL

    SELECT
        chains.start_id,
        exchanges.receiver_id,
        chains.total_gift_value + exchanges.gift_value,
        chains.chain_length + 1
    FROM chains
    JOIN SecretSanta AS exchanges
        ON exchanges.giver_id = chains.current_id
    WHERE chains.current_id <> chains.start_id
),
cycle_stats AS (
    SELECT DISTINCT
        chain_length,
        total_gift_value
    FROM chains
    WHERE current_id = start_id
)
SELECT
    ROW_NUMBER() OVER (
        ORDER BY chain_length DESC, total_gift_value DESC
    ) AS chain_id,
    chain_length,
    total_gift_value
FROM cycle_stats
ORDER BY chain_length DESC, total_gift_value DESC;
