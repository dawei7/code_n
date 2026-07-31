WITH yearly_purchases AS (
    SELECT
        customer_id,
        YEAR(order_date) AS order_year,
        SUM(price) AS total_purchase
    FROM Orders
    GROUP BY customer_id, YEAR(order_date)
),
compared_years AS (
    SELECT
        customer_id,
        order_year,
        total_purchase,
        LAG(total_purchase) OVER (
            PARTITION BY customer_id
            ORDER BY order_year
        ) AS previous_total
    FROM yearly_purchases
)
SELECT customer_id
FROM compared_years
GROUP BY customer_id
HAVING COUNT(*) = MAX(order_year) - MIN(order_year) + 1
   AND SUM(
       CASE
           WHEN previous_total IS NOT NULL
                AND total_purchase <= previous_total THEN 1
           ELSE 0
       END
   ) = 0;
