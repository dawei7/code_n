-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            first_name,
            type,
            TO_CHAR(duration * INTERVAL '1 second', 'HH24:MI:SS') AS duration_formatted,
            RANK() OVER (
                PARTITION BY type
                ORDER BY duration DESC
            ) AS rk
        FROM
            Calls AS c1
            JOIN Contacts AS c2 ON c1.contact_id = c2.id
    )
SELECT
    first_name,
    type,
    duration_formatted
FROM T
WHERE rk <= 3
ORDER BY type DESC, duration_formatted DESC, first_name DESC;
