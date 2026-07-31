# Count Number of Ways to Place Houses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2320 |
| Difficulty | Medium |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-ways-to-place-houses/) |

## Problem Description
### Goal
A street has `n` plots on each of its two sides, for $2n$ plots in total.
Each plot may either remain empty or receive one house. Along either individual
side, two neighboring plots may not both contain houses.

The two sides impose no restriction on one another: houses may occupy the same
numbered plot on opposite sides. Count all distinct placements satisfying the
adjacency rule on both sides, including the placement with no houses. Return
the count modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: The number of plots on each side, with $1\le n\le10^4$.

**Return value**

The number of valid placements across both street sides modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `4`
- Explanation: Each of the two plots is independently empty or occupied.

**Example 2**

- Input: `n = 2`
- Output: `9`
- Explanation: Each side has three legal patterns, and the sides combine
  independently.
