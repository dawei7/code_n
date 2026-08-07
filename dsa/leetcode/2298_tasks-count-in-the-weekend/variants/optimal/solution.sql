SELECT
    SUM(
        CASE
            WHEN CAST(strftime('%w', submit_date) AS INTEGER) IN (0, 6)
            THEN 1 ELSE 0
        END
    ) AS weekend_cnt,
    SUM(
        CASE
            WHEN CAST(strftime('%w', submit_date) AS INTEGER) BETWEEN 1 AND 5
            THEN 1 ELSE 0
        END
    ) AS working_cnt
FROM Tasks;
