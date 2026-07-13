WITH parent_ids AS (
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
)
SELECT
    node.id,
    CASE
        WHEN node.p_id IS NULL THEN 'Root'
        WHEN parent_ids.p_id IS NOT NULL THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree AS node
LEFT JOIN parent_ids
    ON parent_ids.p_id = node.id
ORDER BY node.id;

