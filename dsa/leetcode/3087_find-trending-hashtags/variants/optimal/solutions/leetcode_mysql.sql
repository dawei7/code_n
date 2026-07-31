WITH FebruaryHashtags AS (
    SELECT REGEXP_SUBSTR(tweet, '#[A-Za-z0-9_]+') AS hashtag
    FROM Tweets
    WHERE tweet_date >= '2024-02-01'
      AND tweet_date < '2024-03-01'
)
SELECT
    hashtag,
    COUNT(*) AS hashtag_count
FROM FebruaryHashtags
GROUP BY hashtag
ORDER BY hashtag_count DESC, hashtag DESC
LIMIT 3;
