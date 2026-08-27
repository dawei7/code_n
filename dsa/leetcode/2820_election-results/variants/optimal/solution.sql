-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT candidate, ROUND(SUM(vote), 4) AS tot
        FROM
            (
                SELECT
                    candidate,
                    1.0 / (COUNT(candidate) OVER (PARTITION BY voter)) AS vote
                FROM Votes
                WHERE candidate IS NOT NULL
            ) AS t
        GROUP BY candidate
    ),
    P AS (
        SELECT
            candidate,
            RANK() OVER (ORDER BY tot DESC) AS rk
        FROM T
    )
SELECT candidate
FROM P
WHERE rk = 1
ORDER BY candidate;

