-- Write your PostgreSQL query statement below
SELECT
    i.item_category AS category,
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 1 THEN o.quantity ELSE 0 END) AS "Monday",
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 2 THEN o.quantity ELSE 0 END) AS "Tuesday",
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 3 THEN o.quantity ELSE 0 END) AS "Wednesday",
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 4 THEN o.quantity ELSE 0 END) AS "Thursday",
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 5 THEN o.quantity ELSE 0 END) AS "Friday",
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 6 THEN o.quantity ELSE 0 END) AS "Saturday",
    SUM(CASE WHEN EXTRACT(ISODOW FROM o.order_date) = 7 THEN o.quantity ELSE 0 END) AS "Sunday"
FROM
    Items AS i
    LEFT JOIN Orders AS o ON i.item_id = o.item_id
GROUP BY i.item_category
ORDER BY category;
