SELECT
    SUM(DAYOFWEEK(submit_date) IN (1, 7)) AS weekend_cnt,
    SUM(DAYOFWEEK(submit_date) BETWEEN 2 AND 6) AS working_cnt
FROM Tasks;
