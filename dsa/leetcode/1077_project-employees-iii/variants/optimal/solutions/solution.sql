WITH ranked_assignments AS (
    SELECT
        p.project_id,
        p.employee_id,
        DENSE_RANK() OVER (
            PARTITION BY p.project_id
            ORDER BY e.experience_years DESC
        ) AS experience_rank
    FROM Project AS p
    INNER JOIN Employee AS e
        ON e.employee_id = p.employee_id
)
SELECT project_id, employee_id
FROM ranked_assignments
WHERE experience_rank = 1
ORDER BY project_id, employee_id;
