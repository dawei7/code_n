WITH boundaries AS (
    SELECT
        id,
        height,
        MAX(height) OVER (
            ORDER BY id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS left_max,
        MAX(height) OVER (
            ORDER BY id DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS right_max
    FROM Heights
)
SELECT SUM(LEAST(left_max, right_max) - height) AS total_trapped_water
FROM boundaries;
