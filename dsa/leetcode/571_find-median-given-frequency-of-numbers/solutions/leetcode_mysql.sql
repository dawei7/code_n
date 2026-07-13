WITH frequency_ranges AS (
    SELECT
        num,
        frequency,
        SUM(frequency) OVER (
            ORDER BY num
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS cumulative,
        SUM(frequency) OVER () AS total_frequency
    FROM Numbers
),
middle_values AS (
    SELECT num
    FROM frequency_ranges
    WHERE 2 * cumulative >= total_frequency
      AND 2 * (cumulative - frequency) <= total_frequency
)
SELECT ROUND(AVG(num), 1) AS median
FROM middle_values;

