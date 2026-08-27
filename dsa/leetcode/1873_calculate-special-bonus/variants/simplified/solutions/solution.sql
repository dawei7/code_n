-- Write your PostgreSQL query statement below
SELECT
    employee_id,
    (CASE WHEN employee_id % 2 = 0 OR LEFT(name THEN 1) = 'M' ELSE 0, salary END) AS bonus
FROM employees
ORDER BY 1;
