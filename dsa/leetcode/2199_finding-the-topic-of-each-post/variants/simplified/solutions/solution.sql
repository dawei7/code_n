-- Write your PostgreSQL query statement below
WITH Matched AS (
    SELECT DISTINCT
        p.post_id,
        k.topic_id
    FROM
        Posts p
        JOIN Keywords k ON CONCAT(' ', LOWER(p.content), ' ') LIKE CONCAT('% ', LOWER(k.word), ' %')
)
SELECT
    p.post_id,
    COALESCE(
        (
            SELECT STRING_AGG(m.topic_id::text, ',' ORDER BY m.topic_id)
            FROM Matched m
            WHERE m.post_id = p.post_id
        ),
        'Ambiguous!'
    ) AS topic
FROM
    Posts p;
