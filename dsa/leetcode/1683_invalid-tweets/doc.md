# Invalid Tweets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1683 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/invalid-tweets/) |

## Problem Description
### Goal

The `Tweets` table records the posts in a social-media application. Each row has a unique integer `tweet_id` and its `content`. Content is made from alphanumeric characters, spaces, and exclamation marks, so every stored character—including a space or `!`—contributes to the content length.

A tweet is invalid precisely when its content contains strictly more than 15 characters. Produce the `tweet_id` of every invalid row and no valid row. The result may be returned in any order; content with exactly 15 characters remains valid, while 16 characters is the first invalid length.

### Function Contract
**Inputs**

- `Tweets(tweet_id, content)`: one row per tweet, with `tweet_id` as the primary key

Let $R$ be the number of rows in `Tweets`.

**Return value**

A one-column result table named `tweet_id` containing exactly the IDs whose `content` character count is greater than 15, in any order.

### Examples
**Example 1**

Input table `Tweets`:

| tweet_id | content |
|---:|---|
| 1 | `Let us Code` |
| 2 | `More than fifteen chars are here!` |

Output:

| tweet_id |
|---:|
| 2 |

The two contents have lengths 11 and 33, respectively.

**Example 2**

Input table `Tweets`:

| tweet_id | content |
|---:|---|
| 7 | `123456789012345` |
| 8 | `1234567890123456` |

Output:

| tweet_id |
|---:|
| 8 |

The strict boundary excludes the 15-character row and includes the 16-character row.
