-- Write your PostgreSQL query statement below
SELECT
    m.member_id,
    m.name,
    CASE
        WHEN COUNT(v.visit_id) = 0 THEN 'Bronze'
        WHEN 100 * COUNT(p.charged_amount) / COUNT(v.visit_id) >= 80 THEN 'Diamond'
        WHEN 100 * COUNT(p.charged_amount) / COUNT(v.visit_id) >= 50 THEN 'Gold'
        ELSE 'Silver'
    END AS category
FROM
    Members AS m
    LEFT JOIN Visits AS v ON m.member_id = v.member_id
    LEFT JOIN Purchases AS p ON v.visit_id = p.visit_id
GROUP BY
    m.member_id,
    m.name;
