WITH opinion_stats AS (
    SELECT
        book_id,
        COUNT(*) AS total_sessions,
        MIN(session_rating) AS lowest_rating,
        MAX(session_rating) AS highest_rating,
        SUM(
            CASE
                WHEN session_rating <= 2 OR session_rating >= 4 THEN 1
                ELSE 0
            END
        ) AS extreme_ratings
    FROM reading_sessions
    GROUP BY book_id
    HAVING COUNT(*) >= 5
       AND MIN(session_rating) <= 2
       AND MAX(session_rating) >= 4
       AND SUM(
               CASE
                   WHEN session_rating <= 2 OR session_rating >= 4 THEN 1
                   ELSE 0
               END
           ) >= 0.6 * COUNT(*)
)
SELECT
    books.book_id,
    books.title,
    books.author,
    books.genre,
    books.pages,
    opinion_stats.highest_rating - opinion_stats.lowest_rating AS rating_spread,
    ROUND(1.0 * opinion_stats.extreme_ratings / opinion_stats.total_sessions, 2) AS polarization_score
FROM opinion_stats
JOIN books
    ON books.book_id = opinion_stats.book_id
ORDER BY polarization_score DESC, books.title DESC;
