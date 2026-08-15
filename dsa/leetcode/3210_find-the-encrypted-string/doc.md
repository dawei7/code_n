# Find the Encrypted String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3210 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-encrypted-string/) |

## Problem Description

### Goal

Given a lowercase string `s` and a positive integer `k`, encrypt every position using the circular order of characters in the string itself.

For each character at index `i`, place the character found exactly `k` positions after it into index `i` of the encrypted result. Continue from the beginning whenever the walk passes the final character. All replacements are based on the original string.

Return the resulting encrypted string.

### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters with $1 \le \lvert s\rvert \le 100$.
- `k`: The positive circular offset, with $1 \le k \le 10^4$.

Let $n=\lvert s\rvert$.

**Return value**

- A length-$n$ string whose character at index $i$ is the original character at index $(i+k)\bmod n$.

### Examples

#### Example 1

- **Input:** `s = "dart", k = 3`
- **Output:** `"tdar"`
- **Explanation:** Each position receives the character three circular steps after its original index.

#### Example 2

- **Input:** `s = "aaa", k = 1`
- **Output:** `"aaa"`
- **Explanation:** Rotating equal characters leaves the visible string unchanged.
