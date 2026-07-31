SELECT
    books.book_id,
    books.title,
    books.author,
    books.genre,
    books.publication_year,
    COUNT(*) AS current_borrowers
FROM library_books AS books
JOIN borrowing_records AS records
    ON records.book_id = books.book_id
   AND records.return_date IS NULL
GROUP BY
    books.book_id,
    books.title,
    books.author,
    books.genre,
    books.publication_year,
    books.total_copies
HAVING COUNT(*) = books.total_copies
ORDER BY current_borrowers DESC, books.title ASC;
