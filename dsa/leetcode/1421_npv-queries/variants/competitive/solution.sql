SELECT q.id,
       q.year,
       COALESCE(n.npv, 0) AS npv
FROM Queries AS q
LEFT JOIN NPV AS n
  ON n.id = q.id
 AND n.year = q.year
ORDER BY q.id, q.year;
