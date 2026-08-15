# Find the Lexicographically Largest String From the Box II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3406 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/) |

## Problem Description

### Goal

Alice plays a game with `numFriends` friends using the lowercase string `word`. In every round, she splits `word` into exactly `numFriends` non-empty contiguous strings. A round may use any placement of the cuts that has not appeared in an earlier round, and every resulting piece is placed into a box.

After all distinct splits have been used, return the lexicographically largest string that ever entered the box. At the first position where two strings differ, the string with the later lowercase letter is larger. If one string is a prefix of the other, the longer string is larger.

### Function Contract

**Inputs**

- `word`: A string containing only lowercase English letters.
- `numFriends`: The exact number of non-empty pieces in every split.

The constraints are $1\le \lvert\texttt{word}\rvert\le2\cdot10^5$ and $1\le\texttt{numFriends}\le\lvert\texttt{word}\rvert$.

**Return value**

- The lexicographically largest piece produced across all distinct valid splits.

### Examples

#### Example 1

- **Input:** `word = "dbca", numFriends = 2`
- **Output:** `"dbc"`

The three possible splits are `"d" | "bca"`, `"db" | "ca"`, and `"dbc" | "a"`. The largest piece among them is `"dbc"`.

#### Example 2

- **Input:** `word = "gggg", numFriends = 4`
- **Output:** `"g"`

Every character must be a separate non-empty piece, so the box contains only `"g"`.
