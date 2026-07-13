WITH Sequenced AS (
    SELECT
        id,
        num,
        LAG(num, 1) OVER (ORDER BY id) AS previous_one,
        LAG(num, 2) OVER (ORDER BY id) AS previous_two
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM Sequenced
WHERE num = previous_one
  AND num = previous_two
ORDER BY ConsecutiveNums;
