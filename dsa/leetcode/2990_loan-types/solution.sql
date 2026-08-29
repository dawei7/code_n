-- Write your PostgreSQL query statement below
SELECT user_id
FROM Loans
GROUP BY 1
HAVING SUM(CASE WHEN loan_type = 'Refinance' THEN 1 ELSE 0 END) > 0 AND SUM(CASE WHEN loan_type = 'Mortgage' THEN 1 ELSE 0 END) > 0
ORDER BY 1;
