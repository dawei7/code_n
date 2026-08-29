-- Write your PostgreSQL query statement below
WITH numbered AS (
    SELECT
        id,
        drink,
        ROW_NUMBER() OVER () AS rn
    FROM CoffeeShop
),
grouped AS (
    SELECT
        id,
        drink,
        rn,
        COUNT(drink) OVER (ORDER BY rn) AS grp
    FROM numbered
)
SELECT
    id,
    FIRST_VALUE(drink) OVER (PARTITION BY grp ORDER BY rn) AS drink
FROM grouped
ORDER BY rn;

