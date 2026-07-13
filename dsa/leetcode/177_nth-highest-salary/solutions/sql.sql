SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET (SELECT N - 1 FROM Request LIMIT 1)
) AS getNthHighestSalary;
