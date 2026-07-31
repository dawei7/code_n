WITH RECURSIVE Hashtags AS (
    SELECT
        tweet_id,
        tweet,
        1 AS occurrence,
        REGEXP_SUBSTR(tweet, '#[^ ]+', 1, 1) AS hashtag
    FROM Tweets
    WHERE tweet_date >= '2024-02-01'
      AND tweet_date < '2024-03-01'

    UNION ALL

    SELECT
        tweet_id,
        tweet,
        occurrence + 1,
        REGEXP_SUBSTR(tweet, '#[^ ]+', 1, occurrence + 1)
    FROM Hashtags
    WHERE hashtag IS NOT NULL
)
SELECT
    hashtag,
    COUNT(*) AS count
FROM Hashtags
WHERE hashtag IS NOT NULL
GROUP BY hashtag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
