WITH allocation_metrics AS (
    SELECT
        p.employee_id,
        p.project_id,
        e.name AS employee_name,
        p.workload AS project_workload,
        AVG(p.workload) OVER (PARTITION BY e.team) AS team_average
    FROM Project AS p
    JOIN Employees AS e
        ON e.employee_id = p.employee_id
)
SELECT
    employee_id,
    project_id,
    employee_name,
    project_workload
FROM allocation_metrics
WHERE project_workload > team_average
ORDER BY employee_id ASC, project_id ASC;
