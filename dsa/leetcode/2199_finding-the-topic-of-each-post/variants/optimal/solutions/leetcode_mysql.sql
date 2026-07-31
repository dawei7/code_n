SELECT
    Posts.post_id,
    COALESCE(
        GROUP_CONCAT(
            DISTINCT Keywords.topic_id
            ORDER BY Keywords.topic_id
            SEPARATOR ','
        ),
        'Ambiguous!'
    ) AS topic
FROM Posts
LEFT JOIN Keywords
  ON CONCAT(' ', LOWER(Posts.content), ' ')
     LIKE CONCAT('% ', LOWER(Keywords.word), ' %')
GROUP BY Posts.post_id;
