WITH RECURSIVE converted AS (
    SELECT
        content_id,
        content_text,
        1 AS char_pos,
        1 AS word_start,
        CAST('' AS CHAR(10000)) AS converted_text
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        char_pos + 1,
        CASE
            WHEN SUBSTRING(content_text, char_pos, 1) = ' ' THEN char_pos + 1
            ELSE word_start
        END,
        CONCAT(
            converted_text,
            CASE
                WHEN char_pos = word_start
                    OR (
                        SUBSTRING(content_text, char_pos - 1, 1) = '-'
                        AND SUBSTRING_INDEX(
                            SUBSTRING(content_text, word_start),
                            ' ',
                            1
                        ) REGEXP '^[A-Za-z]+-[A-Za-z]+$'
                    )
                    THEN UPPER(SUBSTRING(content_text, char_pos, 1))
                ELSE LOWER(SUBSTRING(content_text, char_pos, 1))
            END
        )
    FROM converted
    WHERE char_pos <= CHAR_LENGTH(content_text)
)
SELECT
    content_id,
    content_text AS original_text,
    converted_text
FROM converted
WHERE char_pos = CHAR_LENGTH(content_text) + 1
ORDER BY content_id;
