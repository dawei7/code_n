SELECT
    ag.age_bucket,
    ROUND(
        100.0 * SUM(CASE WHEN a.activity_type = 'send' THEN a.time_spent ELSE 0 END)
        / SUM(a.time_spent),
        2
    ) AS send_perc,
    ROUND(
        100.0 * SUM(CASE WHEN a.activity_type = 'open' THEN a.time_spent ELSE 0 END)
        / SUM(a.time_spent),
        2
    ) AS open_perc
FROM Activities AS a
JOIN Age AS ag
    ON ag.user_id = a.user_id
GROUP BY ag.age_bucket;
