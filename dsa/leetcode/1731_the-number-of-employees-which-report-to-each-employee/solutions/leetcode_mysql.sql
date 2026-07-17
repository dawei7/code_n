SELECT
    manager.employee_id,
    manager.name,
    COUNT(report.employee_id) AS reports_count,
    ROUND(AVG(report.age)) AS average_age
FROM Employees AS manager
JOIN Employees AS report
    ON report.reports_to = manager.employee_id
GROUP BY manager.employee_id, manager.name
ORDER BY manager.employee_id ASC;
