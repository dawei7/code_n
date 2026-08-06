## Description

The `Tweets` table stores the author, unique identifier, publication date, and text of each tweet. Every stored date is a valid day in February 2024. Unlike the single-hashtag version of the task, one tweet may contain several hashtags, and every occurrence must contribute to the trend count.

A hashtag begins with `#` and continues through the character immediately before the next space, or through the end of the tweet when no space follows it. Consequently, punctuation and other non-space characters inside that token remain part of the hashtag.

Extract all hashtag occurrences, count equal tokens across the complete table, and return at most the three most frequent hashtags. Order larger counts first. When counts are equal, order the hashtag text itself in descending order.
