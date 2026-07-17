SELECT
    employee_id,
    COALESCE(
        MAX(CASE WHEN primary_flag = 'Y' THEN department_id END),
        MAX(department_id)
    ) AS department_id
FROM Employee
GROUP BY employee_id
ORDER BY employee_id;
