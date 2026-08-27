-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            employee_id,
            SUM(CEIL(EXTRACT(EPOCH FROM (out_time - in_time)) / 60.0)) / 60.0 AS tot
        FROM Logs
        GROUP BY employee_id
    )
SELECT employee_id
FROM
    Employees
    LEFT JOIN T USING (employee_id)
WHERE COALESCE(tot, 0) < needed_hours;
