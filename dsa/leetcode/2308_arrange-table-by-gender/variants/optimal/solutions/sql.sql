SELECT user_id, gender
FROM (
    SELECT
        user_id,
        gender,
        ROW_NUMBER() OVER (
            PARTITION BY gender
            ORDER BY user_id
        ) AS position
    FROM Genders
) AS ranked
ORDER BY
    position,
    CASE gender
        WHEN 'female' THEN 1
        WHEN 'other' THEN 2
        ELSE 3
    END;
