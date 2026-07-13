WITH salary_rows AS (
    SELECT
        DATE_FORMAT(salary.pay_date, '%Y-%m') AS pay_month,
        employee.department_id,
        salary.amount,
        AVG(salary.amount) OVER (
            PARTITION BY DATE_FORMAT(salary.pay_date, '%Y-%m')
        ) AS company_average
    FROM Salary AS salary
    JOIN Employee AS employee
        ON employee.employee_id = salary.employee_id
), department_averages AS (
    SELECT
        pay_month,
        department_id,
        AVG(amount) AS department_average,
        MAX(company_average) AS company_average
    FROM salary_rows
    GROUP BY pay_month, department_id
)
SELECT
    pay_month,
    department_id,
    CASE
        WHEN department_average > company_average THEN 'higher'
        WHEN department_average < company_average THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM department_averages
ORDER BY pay_month, department_id;
