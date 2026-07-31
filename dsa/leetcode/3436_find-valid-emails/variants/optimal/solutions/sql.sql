WITH parsed AS (
    SELECT
        user_id,
        email,
        INSTR(email, '@') AS at_position,
        SUBSTR(email, 1, INSTR(email, '@') - 1) AS local_part,
        SUBSTR(
            email,
            INSTR(email, '@') + 1,
            LENGTH(email) - INSTR(email, '@') - 4
        ) AS domain_part
    FROM Users
)
SELECT user_id, email
FROM parsed
WHERE at_position > 1
  AND SUBSTR(email, -4) = '.com'
  AND INSTR(SUBSTR(email, at_position + 1), '@') = 0
  AND local_part NOT GLOB '*[^A-Za-z0-9_]*'
  AND domain_part <> ''
  AND domain_part NOT GLOB '*[^A-Za-z]*'
ORDER BY user_id;
