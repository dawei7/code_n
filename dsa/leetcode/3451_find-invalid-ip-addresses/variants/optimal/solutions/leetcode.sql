WITH parsed AS (
    SELECT
        ip,
        LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) AS dot_count,
        SUBSTRING_INDEX(ip, '.', 1) AS octet1,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS octet2,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS octet3,
        SUBSTRING_INDEX(ip, '.', -1) AS octet4
    FROM logs
)
SELECT ip, COUNT(*) AS invalid_count
FROM parsed
WHERE dot_count <> 3
   OR ip REGEXP '(^|[.])0[0-9]+'
   OR CAST(octet1 AS UNSIGNED) > 255
   OR CAST(octet2 AS UNSIGNED) > 255
   OR CAST(octet3 AS UNSIGNED) > 255
   OR CAST(octet4 AS UNSIGNED) > 255
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
