# Find the Lexicographically Largest String From the Box I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3403 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/) |

## Problem Description

### Goal

Alice has a string `word` and organizes a game for `numFriends` friends. During a round, she divides `word` into exactly `numFriends` non-empty contiguous strings. Every round must use a different placement of the split boundaries, and all pieces produced in every possible round are placed into a box.

After every distinct split has been used, return the lexicographically largest string present in the box. Pieces do not have to have equal lengths, and their original order inside `word` is preserved. Lexicographic comparison follows the usual lowercase-English-letter ordering; when one string is a prefix of another, the longer string is larger.

### Function Contract

**Inputs**

- `word`: A string containing only lowercase English letters.
- `numFriends`: The exact number of non-empty pieces in every split.

Let $n=\lvert\texttt{word}\rvert$. The constraints are $1\le n\le5000$ and $1\le\texttt{numFriends}\le n$.

**Return value**

- The lexicographically largest piece produced by any valid split of `word`.

### Examples

**Example 1**

- Input: `word = "dbca", numFriends = 2`
- Output: `"dbc"`

The three possible splits produce `("d", "bca")`, `("db", "ca")`, and `("dbc", "a")`. The largest piece among them is `"dbc"`.

**Example 2**

- Input: `word = "gggg", numFriends = 4`
- Output: `"g"`

Every friend must receive one character, so there is only one possible split and every piece equals `"g"`.
