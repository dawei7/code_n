# The Number of Ways to Make the Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3183 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/) |

## Problem Description

### Goal

A coin supply contains unlimited coins of values 1, 2, and 6, but it contains exactly two available coins of value 4. Given a target sum `n`, count the distinct combinations of available coins whose values add to `n`.

Only the number of coins of each value matters. Reordering the same multiset does not create another combination, and a valid combination may use zero, one, or two value-4 coins but never more than two.

Return the number of combinations modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: The target sum, with $1 \le n \le 10^5$.

**Return value**

- The number of order-independent coin combinations totaling `n`, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `4`

The combinations are `[1, 1, 1, 1]`, `[1, 1, 2]`, `[2, 2]`, and `[4]`.

**Example 2**

- Input: `n = 12`
- Output: `22`

A selection such as `[4, 4, 4]` is invalid because only two value-4 coins are available.

**Example 3**

- Input: `n = 5`
- Output: `4`

The combinations are `[1, 1, 1, 1, 1]`, `[1, 1, 1, 2]`, `[1, 2, 2]`, and `[1, 4]`.
