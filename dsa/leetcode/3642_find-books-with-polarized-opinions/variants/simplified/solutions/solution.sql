-- Write your PostgreSQL query statement below
SELECT
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.pages,
    (MAX(r.session_rating) - MIN(r.session_rating)) AS rating_spread,
    ROUND((SUM(CASE WHEN r.session_rating <= 2 THEN 1 ELSE 0 END) + SUM(CASE WHEN r.session_rating >= 4 THEN 1 ELSE 0 END))::numeric / COUNT(1), 2) AS polarization_score
FROM
    books b
    JOIN reading_sessions r USING (book_id)
GROUP BY b.book_id, b.title, b.author, b.genre, b.pages
HAVING
    COUNT(1) >= 5
    AND MAX(r.session_rating) >= 4
    AND MIN(r.session_rating) <= 2
    AND (SUM(CASE WHEN r.session_rating <= 2 THEN 1 ELSE 0 END) + SUM(CASE WHEN r.session_rating >= 4 THEN 1 ELSE 0 END))::numeric / COUNT(1) >= 0.6
ORDER BY polarization_score DESC, b.title DESC;
