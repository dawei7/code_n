-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT generate_series(1, 4) AS week_of_month
    ),
    M AS (
        SELECT 'Premium' AS membership
        UNION ALL
        SELECT 'VIP' AS membership
    ),
    P AS (
        SELECT
            CEIL(EXTRACT(DAY FROM purchase_date) / 7.0)::int AS week_of_month,
            membership,
            amount_spend
        FROM
            Purchases
            JOIN Users USING (user_id)
        WHERE TO_CHAR(purchase_date, 'YYYYMM') = '202311'
          AND EXTRACT(DOW FROM purchase_date) = 5
          AND membership IN ('Premium', 'VIP')
    )
SELECT
    T.week_of_month,
    M.membership,
    COALESCE(SUM(P.amount_spend), 0) AS total_amount
FROM
    T
    CROSS JOIN M
    LEFT JOIN P ON T.week_of_month = P.week_of_month AND M.membership = P.membership
GROUP BY T.week_of_month, M.membership
ORDER BY T.week_of_month, M.membership;
