WITH RECURSIVE converted AS (
    SELECT content_id, content_text, 1 AS char_index,
           CAST('' AS CHAR(1000)) AS converted_text
    FROM user_content

    UNION ALL

    SELECT content_id, content_text, char_index + 1,
           CONCAT(
               converted_text,
               CASE
                   WHEN char_index = 1
                        OR SUBSTR(content_text, char_index - 1, 1) = ' '
                   THEN UPPER(SUBSTR(content_text, char_index, 1))
                   ELSE LOWER(SUBSTR(content_text, char_index, 1))
               END
           )
    FROM converted
    WHERE char_index <= LENGTH(content_text)
)
SELECT content_id,
       content_text AS original_text,
       converted_text
FROM converted
WHERE char_index = LENGTH(content_text) + 1
ORDER BY content_id;
