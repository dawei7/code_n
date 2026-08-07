WITH posts AS (
    SELECT DISTINCT sub_id AS post_id
    FROM Submissions
    WHERE parent_id IS NULL
)
SELECT posts.post_id,
       COUNT(DISTINCT comments.sub_id) AS number_of_comments
FROM posts
LEFT JOIN Submissions AS comments
       ON comments.parent_id = posts.post_id
GROUP BY posts.post_id
ORDER BY posts.post_id;
