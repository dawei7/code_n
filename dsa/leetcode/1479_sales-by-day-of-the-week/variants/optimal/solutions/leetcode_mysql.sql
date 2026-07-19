SELECT
    items.item_category AS Category,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 0 THEN orders.quantity ELSE 0 END) AS Monday,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 1 THEN orders.quantity ELSE 0 END) AS Tuesday,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 2 THEN orders.quantity ELSE 0 END) AS Wednesday,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 3 THEN orders.quantity ELSE 0 END) AS Thursday,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 4 THEN orders.quantity ELSE 0 END) AS Friday,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 5 THEN orders.quantity ELSE 0 END) AS Saturday,
    SUM(CASE WHEN WEEKDAY(orders.order_date) = 6 THEN orders.quantity ELSE 0 END) AS Sunday
FROM Items AS items
LEFT JOIN Orders AS orders
    ON orders.item_id = items.item_id
GROUP BY items.item_category
ORDER BY items.item_category;
