WITH RECURSIVE candidates AS (
    SELECT
        product_id,
        product_name,
        description,
        1 AS start_position
    FROM products
    WHERE LENGTH(description) >= 11

    UNION ALL

    SELECT
        product_id,
        product_name,
        description,
        start_position + 1
    FROM candidates
    WHERE start_position < LENGTH(description) - 10
)
SELECT DISTINCT product_id, product_name, description
FROM candidates
WHERE SUBSTR(description, start_position, 2) GLOB 'SN'
  AND SUBSTR(description, start_position + 2, 4)
      GLOB '[0-9][0-9][0-9][0-9]'
  AND SUBSTR(description, start_position + 6, 1) = '-'
  AND SUBSTR(description, start_position + 7, 4)
      GLOB '[0-9][0-9][0-9][0-9]'
  AND (
      start_position = 1
      OR SUBSTR(description, start_position - 1, 1)
         NOT GLOB '[A-Za-z0-9_]'
  )
  AND (
      start_position + 10 = LENGTH(description)
      OR SUBSTR(description, start_position + 11, 1)
         NOT GLOB '[A-Za-z0-9_]'
  )
ORDER BY product_id;
