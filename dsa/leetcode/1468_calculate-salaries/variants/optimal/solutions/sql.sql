WITH company_rates AS (
    SELECT
        company_id,
        CASE
            WHEN MAX(salary) < 1000 THEN 100
            WHEN MAX(salary) <= 10000 THEN 76
            ELSE 51
        END AS take_home_percent
    FROM Salaries
    GROUP BY company_id
)
SELECT
    salaries.company_id,
    salaries.employee_id,
    salaries.employee_name,
    ROUND(salaries.salary * company_rates.take_home_percent / 100.0) AS salary
FROM Salaries AS salaries
JOIN company_rates
    ON company_rates.company_id = salaries.company_id;
