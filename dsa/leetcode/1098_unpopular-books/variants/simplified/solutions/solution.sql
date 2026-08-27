-- Write your PostgreSQL query statement below
SELECT book_id, name
FROM
    Books
    LEFT JOIN Orders USING (book_id)
WHERE available_from < '2019-05-23'
GROUP BY 1
HAVING SUM((CASE WHEN dispatch_date >= '2018-06-23' THEN quantity ELSE 0 END)) < 10;
