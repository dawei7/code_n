WITH RankedCandidates AS (
    SELECT
        employee_id,
        experience,
        salary,
        SUM(salary) OVER (
            PARTITION BY experience
            ORDER BY salary, employee_id
        ) AS running_salary
    FROM Candidates
),
SeniorBudget AS (
    SELECT
        COUNT(*) AS accepted_seniors,
        COALESCE(MAX(running_salary), 0) AS senior_spending
    FROM RankedCandidates
    WHERE experience = 'Senior'
      AND running_salary <= 70000
)
SELECT
    'Senior' AS experience,
    accepted_seniors AS accepted_candidates
FROM SeniorBudget
UNION ALL
SELECT
    'Junior' AS experience,
    COUNT(*) AS accepted_candidates
FROM RankedCandidates
CROSS JOIN SeniorBudget
WHERE experience = 'Junior'
  AND running_salary <= 70000 - senior_spending;
