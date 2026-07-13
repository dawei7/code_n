SELECT ROUND(
    MIN(SQRT(
        (first_point.x - second_point.x) * (first_point.x - second_point.x)
        + (first_point.y - second_point.y) * (first_point.y - second_point.y)
    )),
    2
) AS shortest
FROM Point2D AS first_point
JOIN Point2D AS second_point
    ON first_point.x < second_point.x
    OR (first_point.x = second_point.x AND first_point.y < second_point.y);
