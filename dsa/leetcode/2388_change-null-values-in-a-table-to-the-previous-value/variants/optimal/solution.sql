WITH RECURSIVE ordered_rows AS (
    SELECT
        id,
        drink,
        ROW_NUMBER() OVER () AS sequence_number
    FROM CoffeeShop
),
filled_rows AS (
    SELECT
        id,
        drink,
        sequence_number
    FROM ordered_rows
    WHERE sequence_number = 1

    UNION ALL

    SELECT
        current_row.id,
        COALESCE(current_row.drink, previous_row.drink) AS drink,
        current_row.sequence_number
    FROM filled_rows AS previous_row
    INNER JOIN ordered_rows AS current_row
        ON current_row.sequence_number = previous_row.sequence_number + 1
)
SELECT
    id,
    drink
FROM filled_rows
ORDER BY sequence_number;
