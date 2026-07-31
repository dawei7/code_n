WITH RankedCalls AS (
    SELECT
        contacts.first_name,
        calls.contact_id,
        calls.type,
        calls.duration,
        ROW_NUMBER() OVER (
            PARTITION BY calls.type
            ORDER BY calls.duration DESC, contacts.first_name DESC, calls.contact_id DESC
        ) AS position
    FROM Calls AS calls
    JOIN Contacts AS contacts
        ON contacts.id = calls.contact_id
)
SELECT
    first_name,
    type,
    printf(
        '%02d:%02d:%02d',
        duration / 3600,
        (duration % 3600) / 60,
        duration % 60
    ) AS duration_formatted
FROM RankedCalls
WHERE position <= 3
ORDER BY type DESC, duration DESC, first_name DESC;
