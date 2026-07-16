SELECT
    first_point.id AS p1,
    second_point.id AS p2,
    ABS(first_point.x_value - second_point.x_value)
        * ABS(first_point.y_value - second_point.y_value) AS area
FROM Points AS first_point
JOIN Points AS second_point
    ON first_point.id < second_point.id
    AND first_point.x_value <> second_point.x_value
    AND first_point.y_value <> second_point.y_value
ORDER BY area DESC, p1, p2;
