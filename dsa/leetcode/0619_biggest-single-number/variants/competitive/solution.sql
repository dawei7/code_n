# Time:  O(n)
# Space: O(n)

SELECT
COALESCE(
    (SELECT
        MAX(num)
    FROM
        (SELECT
            num
        FROM
            number
        GROUP BY num
        HAVING COUNT(num) = 1
        ORDER BY NULL) AS t
    )
    , NULL
) AS num
;

