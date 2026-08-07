WITH first_values AS (
    SELECT
        first_col,
        ROW_NUMBER() OVER (ORDER BY first_col ASC) AS position
    FROM Data
),
second_values AS (
    SELECT
        second_col,
        ROW_NUMBER() OVER (ORDER BY second_col DESC) AS position
    FROM Data
)
SELECT first_values.first_col, second_values.second_col
FROM first_values
JOIN second_values
  ON second_values.position = first_values.position
ORDER BY first_values.position;
