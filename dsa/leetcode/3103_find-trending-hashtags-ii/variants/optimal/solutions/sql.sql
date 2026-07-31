WITH RECURSIVE words AS (
    SELECT
        tweet_id,
        TRIM(tweet) || ' ' AS remaining,
        '' AS word
    FROM Tweets
    WHERE tweet_date >= '2024-02-01'
      AND tweet_date < '2024-03-01'

    UNION ALL

    SELECT
        tweet_id,
        LTRIM(SUBSTR(remaining, INSTR(remaining, ' ') + 1)),
        SUBSTR(remaining, 1, INSTR(remaining, ' ') - 1)
    FROM words
    WHERE remaining <> ''
),
hashtags AS (
    SELECT word AS hashtag
    FROM words
    WHERE word LIKE '#%'
)
SELECT
    hashtag,
    COUNT(*) AS count
FROM hashtags
GROUP BY hashtag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
