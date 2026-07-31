WITH hourly_calls AS (
    SELECT
        city,
        CAST(strftime('%H', call_time) AS INTEGER) AS peak_calling_hour,
        COUNT(*) AS number_of_calls
    FROM Calls
    GROUP BY city, CAST(strftime('%H', call_time) AS INTEGER)
),
ranked_hours AS (
    SELECT
        city,
        peak_calling_hour,
        number_of_calls,
        DENSE_RANK() OVER (
            PARTITION BY city
            ORDER BY number_of_calls DESC
        ) AS calling_rank
    FROM hourly_calls
)
SELECT city, peak_calling_hour, number_of_calls
FROM ranked_hours
WHERE calling_rank = 1
ORDER BY peak_calling_hour DESC, city DESC;
