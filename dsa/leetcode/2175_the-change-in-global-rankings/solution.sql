-- Write your PostgreSQL query statement below
WITH
    P AS (
        SELECT team_id, SUM(points_change) AS delta
        FROM PointsChange
        GROUP BY team_id
    )
SELECT
    team_id,
    name,
    (
        RANK() OVER (ORDER BY points DESC, name) - 
        RANK() OVER (ORDER BY (points + delta) DESC, name)
    )::int AS rank_diff
FROM
    TeamPoints
    JOIN P USING (team_id);
