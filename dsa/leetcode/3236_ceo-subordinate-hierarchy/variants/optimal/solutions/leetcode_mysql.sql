WITH RECURSIVE hierarchy AS (
    SELECT
        employee_id,
        employee_name,
        manager_id,
        salary,
        0 AS hierarchy_level,
        salary AS ceo_salary
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        employee.employee_id,
        employee.employee_name,
        employee.manager_id,
        employee.salary,
        hierarchy.hierarchy_level + 1,
        hierarchy.ceo_salary
    FROM Employees AS employee
    INNER JOIN hierarchy
        ON employee.manager_id = hierarchy.employee_id
)
SELECT
    employee_id AS subordinate_id,
    employee_name AS subordinate_name,
    hierarchy_level,
    salary - ceo_salary AS salary_difference
FROM hierarchy
WHERE hierarchy_level > 0
ORDER BY hierarchy_level, subordinate_id;
