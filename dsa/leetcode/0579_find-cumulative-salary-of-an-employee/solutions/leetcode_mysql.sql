WITH salary_windows AS (
    SELECT
        Id,
        Month,
        SUM(Salary) OVER (
            PARTITION BY Id
            ORDER BY Month
            RANGE BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS Salary,
        MAX(Month) OVER (PARTITION BY Id) AS latest_month
    FROM Employee
)
SELECT Id, Month, Salary
FROM salary_windows
WHERE Month < latest_month
ORDER BY Id ASC, Month DESC;

