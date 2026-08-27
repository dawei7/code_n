-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            city,
            h,
            cnt,
            RANK() OVER (
                PARTITION BY city
                ORDER BY cnt DESC
            ) AS rk
        FROM
            (
                SELECT
                    city,
                    EXTRACT(HOUR FROM call_time)::int AS h,
                    COUNT(1) AS cnt
                FROM Calls
                GROUP BY city, EXTRACT(HOUR FROM call_time)
            ) AS t
    )
SELECT city, h AS peak_calling_hour, cnt AS number_of_calls
FROM T
WHERE rk = 1
ORDER BY peak_calling_hour DESC, city DESC;
