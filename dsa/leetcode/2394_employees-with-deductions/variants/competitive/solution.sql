SELECT
    employees.employee_id
FROM Employees AS employees
LEFT JOIN Logs AS logs
    ON logs.employee_id = employees.employee_id
GROUP BY
    employees.employee_id,
    employees.needed_hours
HAVING COALESCE(
    SUM((
        CAST(strftime('%s', logs.out_time) AS INTEGER)
        - CAST(strftime('%s', logs.in_time) AS INTEGER)
        + 59
    ) / 60),
    0
) < employees.needed_hours * 60;
