## Description

The `Tweets` table records a user, a unique tweet, its publication date, and its text. Every tweet contains exactly one hashtag: a token beginning with `#` and ending at the next space or the end of the text.

Consider only tweets published during February 2024. Extract each qualifying tweet's hashtag, count how many times each hashtag appears, and return the three most frequent hashtags. Rank larger counts first; when two hashtags have equal counts, rank the lexicographically larger hashtag first.
