WITH score_rows AS (
    SELECT first_player AS player_id, first_score AS score
    FROM Matches
    UNION ALL
    SELECT second_player AS player_id, second_score AS score
    FROM Matches
),
totals AS (
    SELECT
        players.group_id,
        players.player_id,
        COALESCE(SUM(score_rows.score), 0) AS total_score
    FROM Players AS players
    LEFT JOIN score_rows ON score_rows.player_id = players.player_id
    GROUP BY players.group_id, players.player_id
),
maximums AS (
    SELECT group_id, MAX(total_score) AS maximum_score
    FROM totals
    GROUP BY group_id
)
SELECT totals.group_id, MIN(totals.player_id) AS player_id
FROM totals
JOIN maximums
  ON maximums.group_id = totals.group_id
 AND maximums.maximum_score = totals.total_score
GROUP BY totals.group_id
ORDER BY totals.group_id;
