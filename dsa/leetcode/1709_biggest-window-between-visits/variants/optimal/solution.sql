-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            user_id,
            (LEAD(visit_date::date - 1, '2021-1-1'::date) OVER (
                    PARTITION BY user_id
                    ORDER BY visit_date
                ),
                visit_date
            ) AS diff
        FROM UserVisits
    )
SELECT user_id, MAX(diff) AS biggest_window
FROM T
GROUP BY 1
ORDER BY 1;
