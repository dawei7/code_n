SELECT prices.product_id,
       ROUND(
           COALESCE(
               SUM(prices.price * sales.units) * 1.0 / SUM(sales.units),
               0
           ),
           2
       ) AS average_price
FROM Prices AS prices
LEFT JOIN UnitsSold AS sales
       ON sales.product_id = prices.product_id
      AND sales.purchase_date BETWEEN prices.start_date AND prices.end_date
GROUP BY prices.product_id
ORDER BY prices.product_id;
