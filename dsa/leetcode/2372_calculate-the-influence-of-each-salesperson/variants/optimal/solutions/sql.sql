SELECT
    sp.salesperson_id,
    sp.name,
    COALESCE(SUM(s.price), 0) AS total
FROM Salesperson AS sp
LEFT JOIN Customer AS c
    ON c.salesperson_id = sp.salesperson_id
LEFT JOIN Sales AS s
    ON s.customer_id = c.customer_id
GROUP BY sp.salesperson_id, sp.name
ORDER BY sp.salesperson_id;
