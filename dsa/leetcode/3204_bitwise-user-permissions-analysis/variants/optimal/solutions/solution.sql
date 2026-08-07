WITH RECURSIVE
numbered AS (
    SELECT
        permissions,
        ROW_NUMBER() OVER () AS rn
    FROM user_permissions
),
combined(rn, common_perms, any_perms) AS (
    SELECT rn, permissions, permissions
    FROM numbered
    WHERE rn = 1

    UNION ALL

    SELECT
        next_row.rn,
        combined.common_perms & next_row.permissions,
        combined.any_perms | next_row.permissions
    FROM combined
    JOIN numbered AS next_row
      ON next_row.rn = combined.rn + 1
)
SELECT common_perms, any_perms
FROM combined
ORDER BY rn DESC
LIMIT 1;

