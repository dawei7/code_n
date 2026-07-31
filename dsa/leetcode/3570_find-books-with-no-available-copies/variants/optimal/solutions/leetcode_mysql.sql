SELECT b.book_id, b.title, b.author, b.genre, b.publication_year,
       COUNT(*) AS current_borrowers
FROM library_books AS b
JOIN borrowing_records AS r
  ON r.book_id = b.book_id
 AND r.return_date IS NULL
GROUP BY b.book_id, b.title, b.author, b.genre, b.publication_year, b.total_copies
HAVING COUNT(*) = b.total_copies
ORDER BY current_borrowers DESC, b.title ASC;
