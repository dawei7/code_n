# Time:  O(nlogn)
# Space: O(n)

SELECT state, STRING_AGG(city ORDER BY city SEPARATOR ', ') AS cities
FROM cities
GROUP BY 1
ORDER BY 1;
