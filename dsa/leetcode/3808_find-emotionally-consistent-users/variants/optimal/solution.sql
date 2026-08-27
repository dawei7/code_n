-- Write your PostgreSQL query statement below
WITH
    t AS (
        SELECT
            user_id,
            reaction,
            COUNT(1) AS cnt
        FROM reactions
        GROUP BY user_id, reaction
    ),
    s AS (
        SELECT
            user_id,
            MAX(cnt) AS mx_cnt,
            ROUND(MAX(cnt)::numeric / SUM(cnt), 2) AS reaction_ratio
        FROM t
        GROUP BY user_id
        HAVING MAX(cnt)::numeric / SUM(cnt) >= 0.60 AND SUM(cnt) >= 5
    )
SELECT user_id, reaction AS dominant_reaction, reaction_ratio
FROM
    s
    JOIN t USING (user_id)
WHERE cnt = mx_cnt
ORDER BY reaction_ratio DESC, user_id ASC;
