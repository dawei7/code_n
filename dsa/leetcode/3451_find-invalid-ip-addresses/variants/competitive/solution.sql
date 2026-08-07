WITH RECURSIVE octets AS (
    SELECT
        log_id,
        ip,
        ip || '.' AS remainder,
        0 AS octet_number,
        NULL AS octet
    FROM logs

    UNION ALL

    SELECT
        log_id,
        ip,
        SUBSTR(remainder, INSTR(remainder, '.') + 1),
        octet_number + 1,
        SUBSTR(remainder, 1, INSTR(remainder, '.') - 1)
    FROM octets
    WHERE remainder <> ''
),
classified AS (
    SELECT
        log_id,
        ip,
        COUNT(octet) AS octet_count,
        MAX(CASE WHEN CAST(octet AS INTEGER) > 255 THEN 1 ELSE 0 END) AS has_large_octet,
        MAX(
            CASE
                WHEN LENGTH(octet) > 1 AND SUBSTR(octet, 1, 1) = '0' THEN 1
                ELSE 0
            END
        ) AS has_leading_zero
    FROM octets
    WHERE octet_number > 0
    GROUP BY log_id, ip
),
invalid_rows AS (
    SELECT ip
    FROM classified
    WHERE octet_count <> 4
       OR has_large_octet = 1
       OR has_leading_zero = 1
)
SELECT ip, COUNT(*) AS invalid_count
FROM invalid_rows
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
