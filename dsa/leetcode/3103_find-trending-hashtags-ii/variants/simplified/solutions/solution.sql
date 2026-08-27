-- Write your PostgreSQL query statement below
WITH hashtags AS (
    SELECT (REGEXP_MATCHES(tweet, '#[A-Za-z0-9_]+', 'g'))[1] AS hashtag
    FROM Tweets
    WHERE tweet_date >= '2024-02-01'
      AND tweet_date < '2024-03-01'
)
SELECT
    hashtag,
    COUNT(*) AS count
FROM hashtags
GROUP BY hashtag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
