# First Letter Capitalization

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3368 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/first-letter-capitalization/) |

## Problem Description

### Goal

The `user_content` table stores a unique `content_id` and a text value `content_text` for each row. Transform every word in each text so that its first letter is uppercase and every remaining letter is lowercase. A word begins at the start of the text or immediately after a space.

Existing spaces are data and must remain unchanged, including leading spaces, trailing spaces, and multiple consecutive spaces. The text contains no special characters. Return one row per source record with its identifier, the untouched source text named `original_text`, and the transformed text named `converted_text`.

### Function Contract

**Inputs**

- `user_content`: A table with unique integer column `content_id` and text column `content_text`.

Let $n$ be the number of rows and define

$$
S=\sum_{r\in\texttt{user_content}}\lvert r.\texttt{content_text}\rvert.
$$

**Return value**

- A result table with columns `content_id`, `original_text`, and `converted_text`, ordered by `content_id` ascending.

### Examples

#### Example 1

- Input row: `(1, "hello world of SQL")`
- Output row: `(1, "hello world of SQL", "Hello World Of Sql")`

#### Example 2

- Input row: `(2, "the QUICK brown fox")`
- Output row: `(2, "the QUICK brown fox", "The Quick Brown Fox")`

#### Example 3

- Input row: `(3, "data science AND machine learning")`
- Output row: `(3, "data science AND machine learning", "Data Science And Machine Learning")`
