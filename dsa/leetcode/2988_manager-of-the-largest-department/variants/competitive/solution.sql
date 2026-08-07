WITH ranked_departments AS (
    SELECT
        dep_id,
        DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS department_rank
    FROM Employees
    GROUP BY dep_id
)
SELECT
    employee.emp_name AS manager_name,
    employee.dep_id
FROM Employees AS employee
INNER JOIN ranked_departments AS department
    ON department.dep_id = employee.dep_id
WHERE department.department_rank = 1
  AND employee.position = 'Manager'
ORDER BY employee.dep_id;
