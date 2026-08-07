WITH RECURSIVE
employee_levels AS (
    SELECT employee_id, employee_name, 1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT employee.employee_id, employee.employee_name, manager.level + 1
    FROM Employees AS employee
    INNER JOIN employee_levels AS manager
        ON employee.manager_id = manager.employee_id
),
reporting_tree AS (
    SELECT
        employee_id AS manager_id,
        employee_id AS member_id,
        salary
    FROM Employees

    UNION ALL

    SELECT
        reporting_tree.manager_id,
        employee.employee_id,
        employee.salary
    FROM reporting_tree
    INNER JOIN Employees AS employee
        ON employee.manager_id = reporting_tree.member_id
)
SELECT
    employee_levels.employee_id,
    employee_levels.employee_name,
    employee_levels.level,
    COUNT(reporting_tree.member_id) - 1 AS team_size,
    SUM(reporting_tree.salary) AS budget
FROM employee_levels
INNER JOIN reporting_tree
    ON reporting_tree.manager_id = employee_levels.employee_id
GROUP BY
    employee_levels.employee_id,
    employee_levels.employee_name,
    employee_levels.level
ORDER BY
    employee_levels.level ASC,
    budget DESC,
    employee_levels.employee_name ASC;
