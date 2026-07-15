WITH distinct_logins AS (
    SELECT DISTINCT id, login_date
    FROM Logins
),
numbered_logins AS (
    SELECT
        id,
        login_date,
        julianday(login_date)
            - ROW_NUMBER() OVER (
                PARTITION BY id
                ORDER BY login_date
            ) AS streak_key
    FROM distinct_logins
),
active_ids AS (
    SELECT DISTINCT id
    FROM numbered_logins
    GROUP BY id, streak_key
    HAVING COUNT(*) >= 5
)
SELECT accounts.id, accounts.name
FROM Accounts AS accounts
JOIN active_ids
    ON active_ids.id = accounts.id
ORDER BY accounts.id;
