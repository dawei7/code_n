WITH monthly_income AS (
    SELECT
        account_id,
        EXTRACT(YEAR_MONTH FROM day) AS income_month,
        SUM(amount) AS total_income
    FROM Transactions
    WHERE type = 'Creditor'
    GROUP BY account_id, EXTRACT(YEAR_MONTH FROM day)
),
over_limit AS (
    SELECT
        monthly_income.account_id,
        monthly_income.income_month
    FROM monthly_income
    INNER JOIN Accounts
        ON Accounts.account_id = monthly_income.account_id
    WHERE monthly_income.total_income > Accounts.max_income
)
SELECT DISTINCT first_month.account_id
FROM over_limit AS first_month
INNER JOIN over_limit AS next_month
    ON next_month.account_id = first_month.account_id
    AND PERIOD_DIFF(next_month.income_month, first_month.income_month) = 1;
