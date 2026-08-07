SELECT
    CAST((minute - 1) / 6 AS INTEGER) + 1 AS interval_no,
    SUM(order_count) AS total_orders
FROM Orders
GROUP BY interval_no
ORDER BY interval_no;
