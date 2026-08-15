# String Compression III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3163 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/string-compression-iii/) |

## Problem Description

### Goal

Compress a nonempty string `word` by repeatedly consuming a prefix from what remains. Each chosen prefix must contain only one repeated character and must be as long as possible without exceeding nine characters.

For every consumed prefix, append its one-digit length followed by its character to an initially empty result string. Continue until all of `word` has been consumed, then return the resulting compression. A run longer than nine characters is therefore divided into consecutive chunks.

### Function Contract

**Inputs**

- `word`: A string containing only lowercase English letters.

Let $n = \lvert\texttt{word}\rvert$. The constraints satisfy $1 \le n \le 2\cdot10^5$.

**Return value**

- The compressed string formed by the required count-character chunks.

### Examples

#### Example 1

- **Input:** `word = "abcde"`
- **Output:** `"1a1b1c1d1e"`

Every maximal equal-character prefix has length one.

#### Example 2

- **Input:** `word = "aaaaaaaaaaaaaabb"`
- **Output:** `"9a5a2b"`

The fourteen `a` characters are consumed as chunks of nine and five, followed by the two-character `b` run.
