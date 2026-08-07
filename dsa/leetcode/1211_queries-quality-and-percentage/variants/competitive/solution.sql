SELECT
    query_name,
    ROUND(AVG(1.0 * rating / position), 2) AS quality,
    ROUND(100 * AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
