SELECT
    warehouse.name AS warehouse_name,
    SUM(
        warehouse.units
        * products.Width
        * products.Length
        * products.Height
    ) AS volume
FROM Warehouse AS warehouse
JOIN Products AS products
  ON products.product_id = warehouse.product_id
GROUP BY warehouse.name;
