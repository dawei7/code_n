WITH reaction_counts AS (
    SELECT user_id, reaction, COUNT(*) AS reaction_count
    FROM reactions
    GROUP BY user_id, reaction
),
user_totals AS (
    SELECT user_id, COUNT(*) AS total_reactions
    FROM reactions
    GROUP BY user_id
    HAVING COUNT(DISTINCT content_id) >= 5
)
SELECT
    rc.user_id,
    rc.reaction AS dominant_reaction,
    ROUND(1.0 * rc.reaction_count / ut.total_reactions, 2) AS reaction_ratio
FROM reaction_counts AS rc
JOIN user_totals AS ut
  ON ut.user_id = rc.user_id
WHERE rc.reaction_count * 5 >= ut.total_reactions * 3
ORDER BY reaction_ratio DESC, rc.user_id ASC;
