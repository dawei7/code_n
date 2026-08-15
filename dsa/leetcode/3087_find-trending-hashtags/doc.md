# Find Trending Hashtags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3087 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [find-trending-hashtags](https://leetcode.com/problems/find-trending-hashtags/) |

## Problem Description

### Goal

The `Tweets` table records a user, a unique tweet, its publication date, and its text. Every tweet contains exactly one hashtag: a token beginning with `#` and ending at the next space or the end of the text.

Consider only tweets published during February 2024. Extract each qualifying tweet's hashtag, count how many times each hashtag appears, and return the three most frequent hashtags. Rank larger counts first; when two hashtags have equal counts, rank the lexicographically larger hashtag first.

### Function Contract

**Inputs**

- `Tweets(user_id, tweet_id, tweet_date, tweet)`: `tweet_id` uniquely identifies a row, `tweet_date` is its publication date, and `tweet` contains the text and its single hashtag.

Let $n$ be the number of February 2024 rows and let

$$
S = \sum_{t \in \texttt{Tweets}} \lvert t.\texttt{tweet} \rvert
$$

over those rows.

**Return value**

- An ordered table with columns `hashtag` and `hashtag_count`, containing at most three rows sorted by `hashtag_count` descending and then `hashtag` descending.

### Examples

#### Example 1

The supplied February rows contain `#HappyDay` three times, `#TechLife` twice, and both `#WorkLife` and `#Nature` once. The first two occupy the leading ranks; the descending hashtag tie break places `#WorkLife` ahead of `#Nature`, so the result is `(#HappyDay, 3)`, `(#TechLife, 2)`, and `(#WorkLife, 1)`.

#### Example 2

A tweet dated `2024-01-31` or `2024-03-01` does not contribute, while every date from `2024-02-01` through `2024-02-29` does.

#### Example 3

For the text `"New #SQL tips today"`, the extracted hashtag is `#SQL`; the words following its next space are not part of the token.
