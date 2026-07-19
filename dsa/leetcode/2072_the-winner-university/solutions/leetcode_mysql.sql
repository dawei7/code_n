SELECT
    CASE
        WHEN ny.excellent > ca.excellent THEN 'New York University'
        WHEN ny.excellent < ca.excellent THEN 'California University'
        ELSE 'No Winner'
    END AS winner
FROM (
    SELECT COUNT(CASE WHEN score >= 90 THEN 1 END) AS excellent
    FROM NewYork
) AS ny
CROSS JOIN (
    SELECT COUNT(CASE WHEN score >= 90 THEN 1 END) AS excellent
    FROM California
) AS ca;
