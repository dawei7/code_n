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

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Scan `Tweets` once and evaluate the character count of `content` for each row. Retain `tweet_id` exactly when that count is greater than 15. SQL's character-length function expresses the predicate directly; the comparison must be `> 15`, not `>= 15`.

Each returned row is valid because it passed the defining strict inequality. Conversely, every invalid tweet is examined by the table scan, satisfies that same inequality, and is therefore returned. Selecting only `tweet_id` produces the required schema, and no ordering clause is necessary because the contract accepts any result order.

#### Complexity detail

The filter examines each of the $R$ rows once. Tweet content is bounded by the schema's `VARCHAR(50)`, so measuring one value takes constant-bounded work and the scan takes $O(R)$ time. Apart from the database engine's result output and scan cursor, the filter maintains no structure that grows with $R$, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Byte-length function:** `LENGTH` is equivalent for this contract's ASCII-like allowed characters, but a character-counting function states the rule more directly and remains correct if multibyte text is later admitted.
- **Order the result:** adding `ORDER BY tweet_id` is unnecessary because any order is valid and can introduce sorting work when no suitable index supplies that order.
- **Exact boundary:** content of length 15 is valid; only lengths strictly greater than 15 qualify.
- **Spaces and punctuation:** spaces and exclamation marks are stored characters and count toward the threshold.
- **No invalid tweets:** the correct output retains the `tweet_id` column and contains zero rows.

</details>
