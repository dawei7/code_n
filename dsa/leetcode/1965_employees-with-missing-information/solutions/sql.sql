SELECT employee_id
FROM (
    SELECT employees.employee_id AS employee_id
    FROM Employees AS employees
    LEFT JOIN Salaries AS salaries
      ON salaries.employee_id = employees.employee_id
    WHERE salaries.employee_id IS NULL

    UNION ALL

    SELECT salaries.employee_id AS employee_id
    FROM Salaries AS salaries
    LEFT JOIN Employees AS employees
      ON employees.employee_id = salaries.employee_id
    WHERE employees.employee_id IS NULL
) AS missing
ORDER BY employee_id;
