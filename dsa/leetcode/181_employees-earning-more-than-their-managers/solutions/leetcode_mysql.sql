SELECT employee.name AS Employee
FROM Employee AS employee
JOIN Employee AS manager
    ON manager.id = employee.managerId
WHERE employee.salary > manager.salary;
