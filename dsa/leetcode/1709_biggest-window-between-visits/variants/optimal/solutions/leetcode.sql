WITH visit_gaps AS (
    SELECT
        user_id,
        visit_date,
        LEAD(visit_date) OVER (
            PARTITION BY user_id
            ORDER BY visit_date
        ) AS next_visit
    FROM UserVisits
)
SELECT
    user_id,
    MAX(DATEDIFF(COALESCE(next_visit, '2021-01-01'), visit_date)) AS biggest_window
FROM visit_gaps
GROUP BY user_id;
