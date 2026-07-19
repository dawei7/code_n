SELECT employee.employee_id
FROM Employees AS employee
LEFT JOIN Employees AS manager
  ON manager.employee_id = employee.manager_id
WHERE employee.salary < 30000
  AND employee.manager_id IS NOT NULL
  AND manager.employee_id IS NULL
ORDER BY employee.employee_id;
