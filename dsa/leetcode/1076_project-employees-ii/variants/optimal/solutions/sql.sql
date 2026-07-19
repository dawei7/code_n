WITH project_counts AS (
    SELECT project_id, COUNT(*) AS employee_count
    FROM Project
    GROUP BY project_id
)
SELECT project_id
FROM project_counts
WHERE employee_count = (SELECT MAX(employee_count) FROM project_counts)
ORDER BY project_id;
