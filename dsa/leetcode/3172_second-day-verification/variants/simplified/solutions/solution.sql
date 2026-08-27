-- Write your PostgreSQL query statement below
SELECT user_id
FROM
    Emails AS e
    JOIN texts AS t
        ON e.email_id = t.email_id
        AND (action_date::date - signup_date::date) = 1
        AND signup_action = 'Verified'
ORDER BY 1;
