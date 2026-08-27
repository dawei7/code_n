-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            driver_id,
            AVG(distance_km::numeric / fuel_consumed) AS half_avg,
            CASE
                WHEN EXTRACT(MONTH FROM trip_date)::int <= 6 THEN 1
                ELSE 2
            END AS half
        FROM trips
        GROUP BY driver_id, (CASE WHEN EXTRACT(MONTH FROM trip_date)::int <= 6 THEN 1 ELSE 2 END)
    )
SELECT
    t1.driver_id,
    d.driver_name,
    ROUND(t1.half_avg, 2) AS first_half_avg,
    ROUND(t2.half_avg, 2) AS second_half_avg,
    ROUND(t2.half_avg - t1.half_avg, 2) AS efficiency_improvement
FROM
    T t1
    JOIN T t2 ON t1.driver_id = t2.driver_id AND t1.half < t2.half AND t1.half_avg < t2.half_avg
    JOIN drivers d ON t1.driver_id = d.driver_id
ORDER BY efficiency_improvement DESC, d.driver_name ASC;
