WITH Weeks AS (
    SELECT 1 AS week_of_month, DATE('2023-11-03') AS friday
    UNION ALL
    SELECT 2, DATE('2023-11-10')
    UNION ALL
    SELECT 3, DATE('2023-11-17')
    UNION ALL
    SELECT 4, DATE('2023-11-24')
),
Memberships AS (
    SELECT 'Premium' AS membership
    UNION ALL
    SELECT 'VIP'
)
SELECT
    w.week_of_month,
    m.membership,
    COALESCE(SUM(p.amount_spend), 0) AS total_amount
FROM Weeks AS w
CROSS JOIN Memberships AS m
LEFT JOIN Users AS u
    ON u.membership = m.membership
LEFT JOIN Purchases AS p
    ON p.user_id = u.user_id
    AND p.purchase_date = w.friday
GROUP BY w.week_of_month, m.membership
ORDER BY w.week_of_month, m.membership;
