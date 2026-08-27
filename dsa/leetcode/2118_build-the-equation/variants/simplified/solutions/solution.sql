-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            power,
            CASE
                WHEN power = 0 THEN (CASE WHEN factor > 0 THEN CONCAT('+', factor) ELSE CAST(factor AS VARCHAR) END)
                WHEN power = 1 THEN CONCAT(
                    (CASE WHEN factor > 0 THEN CONCAT('+', factor) ELSE CAST(factor AS VARCHAR) END),
                    'X'
                )
                ELSE CONCAT(
                    (CASE WHEN factor > 0 THEN CONCAT('+', factor) ELSE CAST(factor AS VARCHAR) END),
                    'X^',
                    power
                )
            END AS it
        FROM Terms
    )
SELECT
    CONCAT(STRING_AGG(it, '' ORDER BY power DESC), '=0') AS equation
FROM T;
