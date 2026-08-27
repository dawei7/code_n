-- Write your PostgreSQL query statement below
SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE
    ip ~ '^[0-9]+(\.[0-9]+)*$'
    AND (
        LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) != 3
        OR ip ~ '(^|\.)0[0-9]'
        OR (
            LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) = 3
            AND (
                SPLIT_PART(ip, '.', 1)::bigint > 255
                OR SPLIT_PART(ip, '.', 2)::bigint > 255
                OR SPLIT_PART(ip, '.', 3)::bigint > 255
                OR SPLIT_PART(ip, '.', 4)::bigint > 255
            )
        )
    )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
