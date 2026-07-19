# Minimum Cost to Separate Sentence Into Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2052 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/) |

## Problem Description

### Goal

A sentence contains lowercase words separated by single spaces. Insert line breaks only between words so that every row contains at most `k` characters. Words must remain intact, appear exactly once in their original order, and retain one space between adjacent words placed on the same row; rows have no leading or trailing spaces.

For a non-final row of length $r$, pay $(k-r)^2$. The last row contributes no cost, regardless of its unused capacity. Return the minimum total cost over every valid placement of line breaks. Every individual word is guaranteed to fit within the row width.

### Function Contract

**Inputs**

- `sentence`: a nonempty string of lowercase words separated by one space, with total length at most $5000$.
- `k`: the maximum row length, where $1 \le k \le 5000$ and every word's length is at most `k`.

Let $w$ be the number of words.

**Return value**

- Return the minimum sum of squared unused widths over all rows except the final row.

### Examples

**Example 1**

- Input: `sentence = "i love leetcode", k = 12`
- Output: `36`
- Explanation: Rows `"i love"` and `"leetcode"` cost $(12-6)^2+0=36$.

**Example 2**

- Input: `sentence = "apples and bananas taste great", k = 7`
- Output: `21`
- Explanation: Each word occupies its own row; only the first four contribute costs.

**Example 3**

- Input: `sentence = "a", k = 5`
- Output: `0`
- Explanation: The only row is also the last row, whose cost is excluded.
