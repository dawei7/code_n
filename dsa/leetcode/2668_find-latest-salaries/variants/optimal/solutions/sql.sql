SELECT emp_id, firstname, lastname, salary, department_id
FROM (
    SELECT Salary.*,
           ROW_NUMBER() OVER (
               PARTITION BY emp_id
               ORDER BY CAST(salary AS UNSIGNED) DESC
           ) AS salary_rank
    FROM Salary
) AS ranked_salaries
WHERE salary_rank = 1
ORDER BY emp_id;
