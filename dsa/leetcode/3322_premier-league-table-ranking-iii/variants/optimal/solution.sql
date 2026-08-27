-- Write your PostgreSQL query statement below
SELECT
    season_id,
    team_id,
    team_name,
    wins * 3 + draws AS points,
    goals_for - goals_against AS goal_difference,
    RANK() OVER (
        PARTITION BY season_id
        ORDER BY wins * 3 + draws DESC, goals_for - goals_against DESC, team_name ASC
    ) AS position
FROM SeasonStats
ORDER BY season_id ASC, position ASC, team_name ASC;
