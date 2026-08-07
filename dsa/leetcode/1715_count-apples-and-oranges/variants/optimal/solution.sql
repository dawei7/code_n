# Write your MySQL query statement below
SELECT
    SUM(COALESCE(b.apple_count, 0) + COALESCE(c.apple_count, 0)) AS apple_count,
    SUM(COALESCE(b.orange_count, 0) + COALESCE(c.orange_count, 0)) AS orange_count
FROM
    Boxes AS b
    LEFT JOIN Chests AS c USING (chest_id);
