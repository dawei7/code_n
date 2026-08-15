# Total Appeal of A String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2262 |
| Difficulty | Hard |
| Topics | Hash Table, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/total-appeal-of-a-string/) |

## Problem Description

### Goal

The appeal of a string is the number of distinct characters it contains. For
example, repeated copies of the same letter contribute only one to that
string's appeal.

Consider every substring of `s`, where a substring is a nonempty contiguous
sequence selected by its start and end positions. Equal substring values from
different positions are still separate substrings and each contributes its own
appeal. Return the sum of the appeal values over all such index ranges.

### Function Contract

**Inputs**

- `s`: A lowercase-English-letter string of length $n$, where $1\le n\le10^5$.

**Return value**

Return

$$
\sum_{0\le i\le j<n}
\left\lvert\left\{\,\texttt{s[t]}:i\le t\le j\,\right\}\right\rvert,
$$

the total distinct-character count across every substring.

### Examples

#### Example 1

- **Input:** `s = "abbca"`
- **Output:** `28`

#### Example 2

- **Input:** `s = "code"`
- **Output:** `20`

#### Example 3

- **Input:** `s = "aaaa"`
- **Output:** `10`
