WITH spending AS (
    SELECT
        s.user_id,
        s.product_id,
        SUM(s.quantity * p.price) AS amount
    FROM Sales AS s
    JOIN Product AS p
      ON p.product_id = s.product_id
    GROUP BY s.user_id, s.product_id
), ranked AS (
    SELECT
        user_id,
        product_id,
        DENSE_RANK() OVER (
            PARTITION BY user_id
            ORDER BY amount DESC
        ) AS position
    FROM spending
)
SELECT user_id, product_id
FROM ranked
WHERE position = 1;
