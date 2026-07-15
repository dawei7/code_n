WITH user_counts AS (
    SELECT u.name, COUNT(r.movie_id) AS rating_count
    FROM Users AS u
    JOIN MovieRating AS r ON r.user_id = u.user_id
    GROUP BY u.user_id, u.name
),
movie_averages AS (
    SELECT m.title, AVG(r.rating) AS average_rating
    FROM Movies AS m
    JOIN MovieRating AS r ON r.movie_id = m.movie_id
    WHERE r.created_at >= '2020-02-01'
      AND r.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title
),
winners AS (
    SELECT (
        SELECT name
        FROM user_counts
        ORDER BY rating_count DESC, name
        LIMIT 1
    ) AS results, 1 AS position
    UNION ALL
    SELECT (
        SELECT title
        FROM movie_averages
        ORDER BY average_rating DESC, title
        LIMIT 1
    ) AS results, 2 AS position
)
SELECT results
FROM winners
ORDER BY position;
