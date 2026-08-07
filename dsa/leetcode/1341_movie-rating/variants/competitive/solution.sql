SELECT results
FROM (
    SELECT top_user.name AS results, 1 AS position
    FROM (
        SELECT u.name, COUNT(*) AS rating_count
        FROM Users AS u
        JOIN MovieRating AS r ON r.user_id = u.user_id
        GROUP BY u.user_id, u.name
        ORDER BY rating_count DESC, u.name
        LIMIT 1
    ) AS top_user

    UNION ALL

    SELECT top_movie.title AS results, 2 AS position
    FROM (
        SELECT m.title, AVG(r.rating) AS average_rating
        FROM Movies AS m
        JOIN MovieRating AS r ON r.movie_id = m.movie_id
        WHERE r.created_at >= '2020-02-01'
          AND r.created_at < '2020-03-01'
        GROUP BY m.movie_id, m.title
        ORDER BY average_rating DESC, m.title
        LIMIT 1
    ) AS top_movie
) AS winners
ORDER BY position;
