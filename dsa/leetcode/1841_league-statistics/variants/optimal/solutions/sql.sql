WITH team_matches AS (
    SELECT
        home_team_id AS team_id,
        home_team_goals AS goal_for,
        away_team_goals AS goal_against
    FROM Matches
    UNION ALL
    SELECT
        away_team_id AS team_id,
        away_team_goals AS goal_for,
        home_team_goals AS goal_against
    FROM Matches
)
SELECT
    teams.team_name,
    COUNT(*) AS matches_played,
    SUM(
        CASE
            WHEN team_matches.goal_for > team_matches.goal_against THEN 3
            WHEN team_matches.goal_for = team_matches.goal_against THEN 1
            ELSE 0
        END
    ) AS points,
    SUM(team_matches.goal_for) AS goal_for,
    SUM(team_matches.goal_against) AS goal_against,
    SUM(team_matches.goal_for - team_matches.goal_against) AS goal_diff
FROM Teams AS teams
INNER JOIN team_matches
    ON team_matches.team_id = teams.team_id
GROUP BY teams.team_id, teams.team_name
ORDER BY points DESC, goal_diff DESC, team_name ASC;
