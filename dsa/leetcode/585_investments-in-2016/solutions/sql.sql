WITH classified AS (
    SELECT
        tiv_2016,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS value_count,
        COUNT(*) OVER (PARTITION BY lat, lon) AS location_count
    FROM Insurance
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM classified
WHERE value_count > 1
  AND location_count = 1;

