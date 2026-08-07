SELECT
    manager.name
FROM Employee AS report
JOIN Employee AS manager
    ON manager.id = report.managerId
GROUP BY manager.id, manager.name
HAVING COUNT(*) >= 5
ORDER BY manager.name, manager.id;

