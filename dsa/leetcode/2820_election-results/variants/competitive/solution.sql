WITH allocated AS (
    SELECT
        candidate,
        COUNT(candidate) OVER (PARTITION BY voter) AS choices
    FROM Votes
),
totals AS (
    SELECT
        candidate,
        SUM(1.0 / choices) AS votes
    FROM allocated
    WHERE candidate IS NOT NULL
    GROUP BY candidate
),
ranked AS (
    SELECT
        candidate,
        DENSE_RANK() OVER (ORDER BY votes DESC) AS vote_rank
    FROM totals
)
SELECT candidate
FROM ranked
WHERE vote_rank = 1
ORDER BY candidate;

