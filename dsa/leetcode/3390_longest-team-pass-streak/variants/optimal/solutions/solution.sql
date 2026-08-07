WITH pass_results AS (
    SELECT
        passing_team.team_name,
        p.time_stamp,
        CASE
            WHEN passing_team.team_name = receiving_team.team_name THEN 1
            ELSE 0
        END AS successful
    FROM Passes AS p
    INNER JOIN Teams AS passing_team
        ON passing_team.player_id = p.pass_from
    INNER JOIN Teams AS receiving_team
        ON receiving_team.player_id = p.pass_to
),
streak_groups AS (
    SELECT
        team_name,
        successful,
        SUM(CASE WHEN successful = 0 THEN 1 ELSE 0 END) OVER (
            PARTITION BY team_name
            ORDER BY time_stamp
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS streak_group
    FROM pass_results
),
streak_lengths AS (
    SELECT
        team_name,
        streak_group,
        SUM(successful) AS streak_length
    FROM streak_groups
    WHERE successful = 1
    GROUP BY team_name, streak_group
)
SELECT
    team_name,
    MAX(streak_length) AS longest_streak
FROM streak_lengths
GROUP BY team_name
ORDER BY team_name;
