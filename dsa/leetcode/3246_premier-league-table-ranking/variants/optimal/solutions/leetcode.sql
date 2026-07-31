WITH scored AS (
    SELECT
        team_id,
        team_name,
        wins * 3 + draws AS points
    FROM TeamStats
)
SELECT
    team_id,
    team_name,
    points,
    RANK() OVER (ORDER BY points DESC) AS position
FROM scored
ORDER BY points DESC, team_name ASC;
