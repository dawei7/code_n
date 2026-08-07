WITH adjacency AS (
    SELECT user_id1 AS user_id, user_id2 AS friend_id
    FROM Friends
    UNION ALL
    SELECT user_id2 AS user_id, user_id1 AS friend_id
    FROM Friends
),
mutual_pairs AS (
    SELECT DISTINCT
        first_neighbors.user_id AS lower_user_id,
        second_neighbors.user_id AS higher_user_id
    FROM adjacency AS first_neighbors
    JOIN adjacency AS second_neighbors
        ON second_neighbors.friend_id = first_neighbors.friend_id
       AND second_neighbors.user_id > first_neighbors.user_id
)
SELECT
    f.user_id1,
    f.user_id2
FROM Friends AS f
LEFT JOIN mutual_pairs AS mutual
    ON mutual.lower_user_id = CASE
        WHEN f.user_id1 < f.user_id2 THEN f.user_id1 ELSE f.user_id2
    END
   AND mutual.higher_user_id = CASE
        WHEN f.user_id1 < f.user_id2 THEN f.user_id2 ELSE f.user_id1
    END
WHERE mutual.lower_user_id IS NULL
ORDER BY f.user_id1 ASC, f.user_id2 ASC;
