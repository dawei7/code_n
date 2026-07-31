WITH RECURSIVE word_ranges AS (
    SELECT
        content_id,
        content_text,
        1 AS word_start,
        CASE
            WHEN INSTR(content_text, ' ') = 0 THEN LENGTH(content_text) + 1
            ELSE INSTR(content_text, ' ')
        END AS word_end
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        word_end + 1,
        CASE
            WHEN INSTR(SUBSTR(content_text, word_end + 1), ' ') = 0
                THEN LENGTH(content_text) + 1
            ELSE word_end + INSTR(SUBSTR(content_text, word_end + 1), ' ')
        END
    FROM word_ranges
    WHERE word_end <= LENGTH(content_text)
),
words AS (
    SELECT
        content_id,
        content_text,
        word_start,
        SUBSTR(content_text, word_start, word_end - word_start) AS word
    FROM word_ranges
),
normalized AS (
    SELECT
        content_id,
        content_text,
        word_start,
        CASE
            WHEN LENGTH(word) - LENGTH(REPLACE(word, '-', '')) = 1
                AND word NOT GLOB '*[^A-Za-z-]*'
                AND SUBSTR(word, 1, 1) <> '-'
                AND SUBSTR(word, -1, 1) <> '-'
            THEN
                UPPER(SUBSTR(word, 1, 1))
                || LOWER(SUBSTR(word, 2, INSTR(word, '-') - 2))
                || '-'
                || UPPER(SUBSTR(word, INSTR(word, '-') + 1, 1))
                || LOWER(SUBSTR(word, INSTR(word, '-') + 2))
            ELSE UPPER(SUBSTR(word, 1, 1)) || LOWER(SUBSTR(word, 2))
        END AS normalized_word
    FROM words
)
SELECT
    content_id,
    content_text AS original_text,
    COALESCE(
        (
            SELECT GROUP_CONCAT(normalized_word, ' ')
            FROM (
                SELECT normalized_word
                FROM normalized AS ordered_words
                WHERE ordered_words.content_id = source.content_id
                ORDER BY word_start
            )
        ),
        ''
    ) AS converted_text
FROM user_content AS source
ORDER BY content_id;
