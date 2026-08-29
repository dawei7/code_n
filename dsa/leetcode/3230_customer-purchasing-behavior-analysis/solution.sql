-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            Transactions.transaction_id,
            Transactions.customer_id,
            Transactions.transaction_date,
            Transactions.amount,
            Products.product_id,
            Products.category
        FROM
            Transactions
            JOIN Products USING (product_id)
    ),
    P AS (
        SELECT
            customer_id,
            category,
            COUNT(*) AS cnt,
            MAX(transaction_date) AS max_date
        FROM T
        GROUP BY customer_id, category
    ),
    R AS (
        SELECT
            customer_id,
            category,
            RANK() OVER (
                PARTITION BY customer_id
                ORDER BY cnt DESC, max_date DESC
            ) AS rk
        FROM P
    )
SELECT
    t.customer_id,
    ROUND(SUM(t.amount), 2) AS total_amount,
    COUNT(1) AS transaction_count,
    COUNT(DISTINCT t.category) AS unique_categories,
    ROUND(AVG(t.amount), 2) AS avg_transaction_amount,
    r.category AS top_category,
    ROUND(COUNT(1) * 10 + SUM(t.amount)::numeric / 100, 2) AS loyalty_score
FROM
    T t
    JOIN R r ON t.customer_id = r.customer_id AND r.rk = 1
GROUP BY t.customer_id, r.category
ORDER BY loyalty_score DESC, t.customer_id ASC;

