-- Write your PostgreSQL query statement below
WITH words AS (
    SELECT
        content_id,
        content_text,
        ordinality AS word_pos,
        word,
        CASE
            WHEN word ~ '^[A-Za-z]+-[A-Za-z]+$' THEN
                UPPER(SUBSTRING(SPLIT_PART(word, '-', 1), 1, 1)) ||
                LOWER(SUBSTRING(SPLIT_PART(word, '-', 1), 2)) ||
                '-' ||
                UPPER(SUBSTRING(SPLIT_PART(word, '-', 2), 1, 1)) ||
                LOWER(SUBSTRING(SPLIT_PART(word, '-', 2), 2))
            WHEN word ~ '^[A-Za-z]' THEN
                UPPER(SUBSTRING(word, 1, 1)) || LOWER(SUBSTRING(word, 2))
            ELSE
                LOWER(word)
        END AS converted_word
    FROM
        user_content,
        UNNEST(STRING_TO_ARRAY(content_text, ' ')) WITH ORDINALITY AS t(word, ordinality)
)
SELECT
    content_id,
    content_text AS original_text,
    STRING_AGG(converted_word, ' ' ORDER BY word_pos) AS converted_text
FROM words
GROUP BY content_id, content_text
ORDER BY content_id;
