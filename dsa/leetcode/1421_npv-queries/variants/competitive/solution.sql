# Time:  O(n)
# Space: O(n)

SELECT a.id, 
       a.year, 
       COALESCE(b.npv, 0) AS npv 
FROM   queries a 
       LEFT JOIN npv b 
              ON a.id = b.id 
                 AND a.year = b.year;
