WITH RankedCandidates AS (
    SELECT
        employee_id,
        experience,
        salary,
        SUM(salary) OVER (
            PARTITION BY experience
            ORDER BY salary
        ) AS running_salary
    FROM Candidates
),
SeniorBudget AS (
    SELECT COALESCE(MAX(running_salary), 0) AS senior_spending
    FROM RankedCandidates
    WHERE experience = 'Senior'
      AND running_salary <= 70000
)
SELECT employee_id
FROM RankedCandidates
CROSS JOIN SeniorBudget
WHERE (
        experience = 'Senior'
        AND running_salary <= 70000
      )
   OR (
        experience = 'Junior'
        AND running_salary <= 70000 - senior_spending
      );
