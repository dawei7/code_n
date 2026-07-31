SELECT
    passing_team.team_name,
    IF(p.time_stamp <= '45:00', 1, 2) AS half_number,
    SUM(
        IF(
            passing_team.team_name = receiving_team.team_name,
            1,
            -1
        )
    ) AS dominance
FROM Passes AS p
INNER JOIN Teams AS passing_team
    ON passing_team.player_id = p.pass_from
INNER JOIN Teams AS receiving_team
    ON receiving_team.player_id = p.pass_to
GROUP BY passing_team.team_name, half_number
ORDER BY passing_team.team_name, half_number;
