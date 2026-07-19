SELECT b.book_id, b.name
FROM Books AS b
LEFT JOIN Orders AS o
    ON o.book_id = b.book_id
   AND o.dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
WHERE b.available_from < '2019-05-23'
GROUP BY b.book_id, b.name
HAVING COALESCE(SUM(o.quantity), 0) < 10
ORDER BY b.book_id;
