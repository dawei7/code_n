SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 140
   OR CHAR_LENGTH(content) - CHAR_LENGTH(REPLACE(content, '@', '')) > 3
   OR CHAR_LENGTH(content) - CHAR_LENGTH(REPLACE(content, '#', '')) > 3
ORDER BY tweet_id ASC;
