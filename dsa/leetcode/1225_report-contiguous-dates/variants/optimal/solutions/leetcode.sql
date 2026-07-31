WITH periods AS (
    SELECT fail_date AS period_date, 'failed' AS period_state
    FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL
    SELECT success_date AS period_date, 'succeeded' AS period_state
    FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),
islands AS (
    SELECT period_state,
           period_date,
           DATE_SUB(
               period_date,
               INTERVAL ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY period_date) DAY
           ) AS island_key
    FROM periods
)
SELECT period_state,
       MIN(period_date) AS start_date,
       MAX(period_date) AS end_date
FROM islands
GROUP BY period_state, island_key
ORDER BY start_date;
