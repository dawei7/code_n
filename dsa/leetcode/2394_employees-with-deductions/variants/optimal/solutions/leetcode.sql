SELECT
    employees.employee_id
FROM Employees AS employees
LEFT JOIN Logs AS logs
    ON logs.employee_id = employees.employee_id
GROUP BY
    employees.employee_id,
    employees.needed_hours
HAVING COALESCE(
    SUM(CEIL(TIMESTAMPDIFF(SECOND, logs.in_time, logs.out_time) / 60)),
    0
) < employees.needed_hours * 60;
