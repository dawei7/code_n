WITH matched AS (
    SELECT DISTINCT
        Posts.post_id,
        Keywords.topic_id
    FROM Posts
    JOIN Keywords
      ON INSTR(
             ' ' || LOWER(Posts.content) || ' ',
             ' ' || LOWER(Keywords.word) || ' '
         ) > 0
),
ordered_matches AS (
    SELECT
        post_id,
        topic_id
    FROM matched
    ORDER BY post_id, topic_id
),
topics AS (
    SELECT
        post_id,
        GROUP_CONCAT(topic_id, ',') AS topic
    FROM ordered_matches
    GROUP BY post_id
)
SELECT
    Posts.post_id,
    COALESCE(topics.topic, 'Ambiguous!') AS topic
FROM Posts
LEFT JOIN topics
  ON topics.post_id = Posts.post_id;
