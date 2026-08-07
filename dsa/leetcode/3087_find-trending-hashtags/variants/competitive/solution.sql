WITH february AS (
    SELECT SUBSTR(tweet, INSTR(tweet, '#')) AS hashtag_tail
    FROM Tweets
    WHERE tweet_date >= '2024-02-01'
      AND tweet_date < '2024-03-01'
),
hashtags AS (
    SELECT CASE
        WHEN INSTR(hashtag_tail, ' ') = 0 THEN hashtag_tail
        ELSE SUBSTR(hashtag_tail, 1, INSTR(hashtag_tail, ' ') - 1)
    END AS hashtag
    FROM february
)
SELECT
    hashtag,
    COUNT(*) AS hashtag_count
FROM hashtags
GROUP BY hashtag
ORDER BY hashtag_count DESC, hashtag DESC
LIMIT 3;
