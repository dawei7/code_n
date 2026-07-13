WITH Ranked AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM Employee AS e
    INNER JOIN Department AS d
        ON d.id = e.departmentId
)
SELECT Department, Employee, Salary
FROM Ranked
WHERE salary_rank <= 3;
