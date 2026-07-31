WITH purchase_details AS (
    SELECT
        t.customer_id,
        t.transaction_date,
        t.amount,
        p.category
    FROM Transactions AS t
    INNER JOIN Products AS p
        ON p.product_id = t.product_id
),
category_counts AS (
    SELECT
        customer_id,
        category,
        COUNT(*) AS purchase_count,
        MAX(transaction_date) AS latest_transaction
    FROM purchase_details
    GROUP BY customer_id, category
),
ranked_categories AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY purchase_count DESC, latest_transaction DESC, category
        ) AS category_rank
    FROM category_counts
),
customer_totals AS (
    SELECT
        customer_id,
        ROUND(SUM(amount), 2) AS total_amount,
        COUNT(*) AS transaction_count,
        COUNT(DISTINCT category) AS unique_categories,
        ROUND(AVG(amount), 2) AS avg_transaction_amount,
        ROUND(COUNT(*) * 10 + SUM(amount) / 100, 2) AS loyalty_score
    FROM purchase_details
    GROUP BY customer_id
)
SELECT
    totals.customer_id,
    totals.total_amount,
    totals.transaction_count,
    totals.unique_categories,
    totals.avg_transaction_amount,
    categories.category AS top_category,
    totals.loyalty_score
FROM customer_totals AS totals
INNER JOIN ranked_categories AS categories
    ON categories.customer_id = totals.customer_id
   AND categories.category_rank = 1
ORDER BY totals.loyalty_score DESC, totals.customer_id;
