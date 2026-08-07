# Write your MySQL query statement below
SELECT q.*, COALESCE(npv, 0) AS npv
FROM
    Queries AS q
    LEFT JOIN NPV AS n USING (id, year);
