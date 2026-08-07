SELECT user_id
FROM Loans
GROUP BY user_id
HAVING COUNT(DISTINCT CASE
    WHEN loan_type IN ('Mortgage', 'Refinance') THEN loan_type
END) = 2
ORDER BY user_id;
