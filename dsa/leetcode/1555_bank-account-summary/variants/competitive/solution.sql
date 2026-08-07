WITH balance_changes AS (
    SELECT paid_by AS user_id, -amount AS credit_change
    FROM Transactions
    UNION ALL
    SELECT paid_to AS user_id, amount AS credit_change
    FROM Transactions
),
net_changes AS (
    SELECT user_id, SUM(credit_change) AS credit_change
    FROM balance_changes
    GROUP BY user_id
)
SELECT
    users.user_id,
    users.user_name,
    users.credit + COALESCE(net_changes.credit_change, 0) AS credit,
    CASE
        WHEN users.credit + COALESCE(net_changes.credit_change, 0) < 0
            THEN 'Yes'
        ELSE 'No'
    END AS credit_limit_breached
FROM Users AS users
LEFT JOIN net_changes
  ON net_changes.user_id = users.user_id
ORDER BY users.user_id ASC;

