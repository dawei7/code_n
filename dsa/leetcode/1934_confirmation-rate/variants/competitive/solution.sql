SELECT
    signup.user_id,
    ROUND(
        COALESCE(
            AVG(
                CASE
                    WHEN confirmation.action = 'confirmed' THEN 1.0
                    WHEN confirmation.action = 'timeout' THEN 0.0
                END
            ),
            0
        ),
        2
    ) AS confirmation_rate
FROM Signups AS signup
LEFT JOIN Confirmations AS confirmation
    ON confirmation.user_id = signup.user_id
GROUP BY signup.user_id;
