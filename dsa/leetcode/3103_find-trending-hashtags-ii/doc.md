# Find Trending Hashtags II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3103 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [find-trending-hashtags-ii](https://leetcode.com/problems/find-trending-hashtags-ii/) |

## Problem Description

### Goal

The `Tweets` table stores the author, unique identifier, publication date, and text of each tweet. Every stored date is a valid day in February 2024. Unlike the single-hashtag version of the task, one tweet may contain several hashtags, and every occurrence must contribute to the trend count.

A hashtag begins with `#` and continues through the character immediately before the next space, or through the end of the tweet when no space follows it. Consequently, punctuation and other non-space characters inside that token remain part of the hashtag.

Extract all hashtag occurrences, count equal tokens across the complete table, and return at most the three most frequent hashtags. Order larger counts first. When counts are equal, order the hashtag text itself in descending order.

### Function Contract

**Inputs**

- `Tweets(user_id, tweet_id, tweet_date, tweet)`: `tweet_id` is the table's primary key; each row records one user's tweet and its February 2024 date.

Let $S$ be the total number of characters in all tweet texts, $h$ the total number of hashtag occurrences, and $g$ the number of distinct hashtags.

**Return value**

- An ordered table with columns `hashtag` and `count`, containing at most three rows sorted by `count` descending and then `hashtag` descending.

### Examples

#### Example 1

The supplied table contains `#HappyDay` three times and `#TechLife` twice. Every other hashtag occurs once; the descending hashtag tie break selects `#WorkLife` for third place. The result is `(#HappyDay, 3)`, `(#TechLife, 2)`, and `(#WorkLife, 1)`.

#### Example 2

The tweet `"Updates #SQL #Database"` contributes one occurrence to each of `#SQL` and `#Database`, rather than only its first or last hashtag.

#### Example 3

If a tweet ends with `#Launch,`, the comma is part of the non-space hashtag token, so the extracted value is `#Launch,`.
