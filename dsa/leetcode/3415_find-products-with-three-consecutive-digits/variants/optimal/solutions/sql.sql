SELECT product_id, name
FROM Products
WHERE ('x' || name || 'x')
      GLOB '*[^0-9][0-9][0-9][0-9][^0-9]*'
ORDER BY product_id;
