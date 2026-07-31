WITH half_year_efficiency AS (
    SELECT
        driver_id,
        AVG(
            CASE
                WHEN CAST(strftime('%m', trip_date) AS INTEGER) BETWEEN 1 AND 6
                THEN distance_km / fuel_consumed
            END
        ) AS first_half_avg,
        AVG(
            CASE
                WHEN CAST(strftime('%m', trip_date) AS INTEGER) BETWEEN 7 AND 12
                THEN distance_km / fuel_consumed
            END
        ) AS second_half_avg
    FROM trips
    GROUP BY driver_id
)
SELECT
    d.driver_id,
    d.driver_name,
    ROUND(h.first_half_avg, 2) AS first_half_avg,
    ROUND(h.second_half_avg, 2) AS second_half_avg,
    ROUND(h.second_half_avg - h.first_half_avg, 2) AS efficiency_improvement
FROM half_year_efficiency AS h
JOIN drivers AS d
    ON d.driver_id = h.driver_id
WHERE h.first_half_avg IS NOT NULL
  AND h.second_half_avg IS NOT NULL
  AND h.second_half_avg > h.first_half_avg
ORDER BY efficiency_improvement DESC, d.driver_name ASC;
