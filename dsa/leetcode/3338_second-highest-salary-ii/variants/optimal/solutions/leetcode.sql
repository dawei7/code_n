WITH ranked_salaries AS (
    SELECT
        emp_id,
        dept,
        DENSE_RANK() OVER (
            PARTITION BY dept
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)
SELECT emp_id, dept
FROM ranked_salaries
WHERE salary_rank = 2
ORDER BY emp_id ASC;
