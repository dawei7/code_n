WITH marked_matches AS (
    SELECT
        player_id,
        result,
        SUM(result <> 'Win') OVER (
            PARTITION BY player_id
            ORDER BY match_day
        ) AS segment_id
    FROM Matches
),
winning_streaks AS (
    SELECT
        player_id,
        segment_id,
        COUNT(*) AS streak_length
    FROM marked_matches
    WHERE result = 'Win'
    GROUP BY player_id, segment_id
),
players AS (
    SELECT DISTINCT player_id
    FROM Matches
)
SELECT
    players.player_id,
    COALESCE(MAX(winning_streaks.streak_length), 0) AS longest_streak
FROM players
LEFT JOIN winning_streaks
  ON winning_streaks.player_id = players.player_id
GROUP BY players.player_id;
