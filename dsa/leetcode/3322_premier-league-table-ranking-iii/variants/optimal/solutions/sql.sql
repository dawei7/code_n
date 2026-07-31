WITH team_metrics AS (
    SELECT
        season_id,
        team_id,
        team_name,
        wins * 3 + draws AS points,
        goals_for - goals_against AS goal_difference
    FROM SeasonStats
),
ranked_teams AS (
    SELECT
        season_id,
        team_id,
        team_name,
        points,
        goal_difference,
        ROW_NUMBER() OVER (
            PARTITION BY season_id
            ORDER BY points DESC, goal_difference DESC, team_name ASC
        ) AS position
    FROM team_metrics
)
SELECT
    season_id,
    team_id,
    team_name,
    points,
    goal_difference,
    position
FROM ranked_teams
ORDER BY season_id ASC, position ASC, team_name ASC;
