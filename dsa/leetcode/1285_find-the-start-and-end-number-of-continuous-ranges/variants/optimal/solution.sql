-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            log_id,
            SUM(delta) OVER (ORDER BY log_id) AS pid
        FROM
            (
                SELECT
                    log_id,
                    (CASE WHEN (log_id - LAG(log_id) OVER (ORDER BY log_id)) = 1 THEN 0 ELSE 1 END) AS delta
                FROM Logs
            ) AS t
    )
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM T
GROUP BY pid;
