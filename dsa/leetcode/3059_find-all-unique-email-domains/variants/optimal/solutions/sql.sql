WITH extracted AS (
    SELECT SUBSTR(email, INSTR(email, '@') + 1) AS email_domain
    FROM Emails
)
SELECT
    email_domain,
    COUNT(*) AS count
FROM extracted
WHERE email_domain LIKE '%.com'
GROUP BY email_domain
ORDER BY email_domain ASC;
