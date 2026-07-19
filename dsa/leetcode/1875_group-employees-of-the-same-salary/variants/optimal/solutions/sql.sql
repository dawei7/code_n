WITH salary_counts AS (
    SELECT salary, COUNT(*) AS employee_count
    FROM Employees
    GROUP BY salary
)
SELECT
    e.employee_id,
    e.name,
    e.salary,
    DENSE_RANK() OVER (ORDER BY e.salary) AS team_id
FROM Employees AS e
JOIN salary_counts AS c
  ON c.salary = e.salary
WHERE c.employee_count > 1
ORDER BY team_id, e.employee_id;
