WITH RECURSIVE converted AS (
    SELECT
        content_id,
        content_text,
        1 AS char_pos,
        1 AS word_start,
        CAST('' AS TEXT) AS converted_text
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        char_pos + 1,
        CASE
            WHEN SUBSTR(content_text, char_pos, 1) = ' ' THEN char_pos + 1
            ELSE word_start
        END,
        converted_text ||
        CASE
            WHEN char_pos = word_start
                OR (
                    SUBSTR(content_text, char_pos - 1, 1) = '-'
                    AND LENGTH(
                        SUBSTR(
                            content_text,
                            word_start,
                            CASE
                                WHEN INSTR(SUBSTR(content_text, word_start), ' ') = 0
                                THEN LENGTH(content_text) - word_start + 1
                                ELSE INSTR(SUBSTR(content_text, word_start), ' ') - 1
                            END
                        )
                    ) - LENGTH(
                        REPLACE(
                            SUBSTR(
                                content_text,
                                word_start,
                                CASE
                                    WHEN INSTR(SUBSTR(content_text, word_start), ' ') = 0
                                    THEN LENGTH(content_text) - word_start + 1
                                    ELSE INSTR(SUBSTR(content_text, word_start), ' ') - 1
                                END
                            ),
                            '-',
                            ''
                        )
                    ) = 1
                    AND SUBSTR(
                        content_text,
                        word_start,
                        CASE
                            WHEN INSTR(SUBSTR(content_text, word_start), ' ') = 0
                            THEN LENGTH(content_text) - word_start + 1
                            ELSE INSTR(SUBSTR(content_text, word_start), ' ') - 1
                        END
                    ) NOT GLOB '*[^A-Za-z-]*'
                    AND SUBSTR(content_text, word_start, 1) <> '-'
                    AND SUBSTR(
                        SUBSTR(
                            content_text,
                            word_start,
                            CASE
                                WHEN INSTR(SUBSTR(content_text, word_start), ' ') = 0
                                THEN LENGTH(content_text) - word_start + 1
                                ELSE INSTR(SUBSTR(content_text, word_start), ' ') - 1
                            END
                        ),
                        -1,
                        1
                    ) <> '-'
                )
                THEN UPPER(SUBSTR(content_text, char_pos, 1))
            ELSE LOWER(SUBSTR(content_text, char_pos, 1))
        END
    FROM converted
    WHERE char_pos <= LENGTH(content_text)
)
SELECT
    content_id,
    content_text AS original_text,
    converted_text
FROM converted
WHERE char_pos = LENGTH(content_text) + 1
ORDER BY content_id;
