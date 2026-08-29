-- Write your PostgreSQL query statement below
SELECT
    COUNT(*) FILTER (WHERE EXTRACT(ISODOW FROM submit_date) IN (6, 7)) AS weekend_cnt,
    COUNT(*) FILTER (WHERE EXTRACT(ISODOW FROM submit_date) NOT IN (6, 7)) AS working_cnt
FROM Tasks;
