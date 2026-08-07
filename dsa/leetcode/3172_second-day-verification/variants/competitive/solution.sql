SELECT DISTINCT e.user_id
FROM emails AS e
JOIN texts AS t
    ON t.email_id = e.email_id
WHERE t.signup_action = 'Verified'
  AND DATE(t.action_date) = DATE(e.signup_date, '+1 day')
ORDER BY e.user_id;
