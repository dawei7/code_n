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
    CAST(
        MAX(
            julianday(COALESCE(next_visit, '2021-01-01'))
            - julianday(visit_date)
        ) AS INTEGER
    ) AS biggest_window
FROM visit_gaps
GROUP BY user_id;
