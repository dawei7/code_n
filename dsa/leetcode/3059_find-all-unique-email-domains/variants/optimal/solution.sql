-- Write your PostgreSQL query statement below
SELECT
    SPLIT_PART(email, '@', 2) AS email_domain,
    COUNT(*) AS count
FROM Emails
WHERE email LIKE '%.com'
GROUP BY SPLIT_PART(email, '@', 2)
ORDER BY email_domain ASC;

