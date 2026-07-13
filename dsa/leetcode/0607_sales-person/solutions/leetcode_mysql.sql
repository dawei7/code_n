WITH red_sellers AS (
    SELECT DISTINCT orders.sales_id
    FROM Orders AS orders
    JOIN Company AS company
        ON company.com_id = orders.com_id
    WHERE company.name = 'RED'
)
SELECT salesperson.name
FROM SalesPerson AS salesperson
LEFT JOIN red_sellers
    ON red_sellers.sales_id = salesperson.sales_id
WHERE red_sellers.sales_id IS NULL
ORDER BY salesperson.name, salesperson.sales_id;

