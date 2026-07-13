WITH ranked AS (
    SELECT
        id,
        company,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY company
            ORDER BY salary, id
        ) AS salary_row,
        COUNT(*) OVER (
            PARTITION BY company
        ) AS employee_count
    FROM Employee
)
SELECT
    id,
    company,
    salary
FROM ranked
WHERE employee_count <= 2 * salary_row
  AND 2 * salary_row <= employee_count + 2
ORDER BY company, salary, id;

