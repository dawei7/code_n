# Invalid Tweets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3150 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/invalid-tweets-ii/) |

## Problem Description
### Goal
The `Tweets` table stores the identifier and text of every tweet in a social-media application. A tweet is invalid when at least one of three independent limits is exceeded: its content contains more than 140 characters, it contains more than three mentions, or it contains more than three hashtags.

Find every invalid tweet and return its identifier only. A row satisfying several invalidity rules must still appear once. Sort the resulting rows by `tweet_id` in ascending order.

### Function Contract
**Inputs**

- `Tweets`: A table containing one row per tweet.

`Tweets.tweet_id` is an integer primary key. `Tweets.content` is the tweet's varchar text. Each `@` marker denotes a mention and each `#` marker denotes a hashtag for the counting rules.

**Return value**

Return a table with the single column `tweet_id`, containing every tweet that violates at least one limit and ordered by `tweet_id` ascending.

### Examples
**Example 1**

- Input: `Tweets = [(1, "Update @A @B @C @D"), (2, "News #One #Two #Three"), (4, "Work #A #B #C #D")]`
- Output: `[[1], [4]]`
- Explanation: Tweets `1` and `4` contain four mention or hashtag markers; tweet `2` has exactly three hashtags and remains valid.

**Example 2**

- Input: one tweet whose `content` has exactly 140 characters and one whose content has 141 characters
- Output: only the identifier of the 141-character tweet

**Example 3**

- Input: an empty `Tweets` table
- Output: an empty result table with column `tweet_id`
