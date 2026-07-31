WITH pair_counts AS (
    SELECT
        first_relation.user_id AS user1_id,
        second_relation.user_id AS user2_id,
        COUNT(*) AS common_followers
    FROM Relations AS first_relation
    JOIN Relations AS second_relation
      ON second_relation.follower_id = first_relation.follower_id
     AND first_relation.user_id < second_relation.user_id
    GROUP BY first_relation.user_id, second_relation.user_id
),
ranked_pairs AS (
    SELECT
        user1_id,
        user2_id,
        DENSE_RANK() OVER (
            ORDER BY common_followers DESC
        ) AS score_rank
    FROM pair_counts
)
SELECT user1_id, user2_id
FROM ranked_pairs
WHERE score_rank = 1;
