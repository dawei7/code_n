WITH scored AS (
    SELECT
        team_name,
        wins * 3 + draws AS points
    FROM TeamStats
),
ranked AS (
    SELECT
        team_name,
        points,
        RANK() OVER (ORDER BY points DESC) AS position,
        COUNT(*) OVER () AS team_count
    FROM scored
)
SELECT
    team_name,
    points,
    position,
    CASE
        WHEN position <= CEIL(team_count * 0.33) THEN 'Tier 1'
        WHEN position <= CEIL(team_count * 0.66) THEN 'Tier 2'
        ELSE 'Tier 3'
    END AS tier
FROM ranked
ORDER BY points DESC, team_name ASC;
