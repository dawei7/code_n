-- Write your PostgreSQL query statement below
SELECT
    (REGEXP_MATCH(tweet, '#[A-Za-z0-9_]+'))[1] AS hashtag,
    COUNT(*) AS hashtag_count
FROM Tweets
WHERE TO_CHAR(tweet_date, 'YYYYMM') = '202402'
GROUP BY (REGEXP_MATCH(tweet, '#[A-Za-z0-9_]+'))[1]
ORDER BY hashtag_count DESC, hashtag DESC
LIMIT 3;
