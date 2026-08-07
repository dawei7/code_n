SELECT
    employee.name,
    bonus.bonus
FROM Employee AS employee
LEFT JOIN Bonus AS bonus
    ON bonus.empId = employee.empId
WHERE bonus.bonus < 1000
   OR bonus.bonus IS NULL
ORDER BY employee.name, employee.empId;

