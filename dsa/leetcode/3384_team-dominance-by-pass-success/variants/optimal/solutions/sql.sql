SELECT
    passing_team.team_name,
    CASE WHEN p.time_stamp <= '45:00' THEN 1 ELSE 2 END AS half_number,
    SUM(
        CASE
            WHEN passing_team.team_name = receiving_team.team_name THEN 1
            ELSE -1
        END
    ) AS dominance
FROM Passes AS p
INNER JOIN Teams AS passing_team
    ON passing_team.player_id = p.pass_from
INNER JOIN Teams AS receiving_team
    ON receiving_team.player_id = p.pass_to
GROUP BY passing_team.team_name, half_number
ORDER BY passing_team.team_name, half_number;
