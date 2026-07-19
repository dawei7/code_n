WITH point_events AS (
    SELECT host_team AS team_id,
           CASE WHEN host_goals > guest_goals THEN 3 WHEN host_goals = guest_goals THEN 1 ELSE 0 END AS points
    FROM Matches
    UNION ALL
    SELECT guest_team AS team_id,
           CASE WHEN guest_goals > host_goals THEN 3 WHEN guest_goals = host_goals THEN 1 ELSE 0 END AS points
    FROM Matches
)
SELECT teams.team_id, teams.team_name, COALESCE(SUM(point_events.points), 0) AS num_points
FROM Teams AS teams
LEFT JOIN point_events ON point_events.team_id = teams.team_id
GROUP BY teams.team_id, teams.team_name
ORDER BY num_points DESC, teams.team_id ASC;
