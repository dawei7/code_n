# Number of Integers With Popcount-Depth Equal to K I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3621 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Bit Manipulation, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/) |

## Problem Description

### Goal

For a positive integer `x`, begin with $p_0=x$ and repeatedly replace the current value by its popcount, the number of set bits in its binary representation. This process eventually reaches 1. The popcount-depth of `x` is the smallest index $d\ge 0$ for which $p_d=1$; in particular, 1 itself has depth 0.

Given `n` and `k`, count the integers `x` in the inclusive range $[1,n]$ whose popcount-depth is exactly `k`.

### Function Contract

**Inputs**

- `n`: The inclusive upper bound of the range to examine.
- `k`: The exact required popcount-depth.

The constraints are $1 \le n \le 10^{15}$ and $0 \le k \le 5$.

**Return value**

Return the number of positive integers no greater than `n` whose popcount-depth equals `k`.

### Examples

#### Example 1

- **Input:** `n = 4, k = 1`
- **Output:** `2`
- **Explanation:** The qualifying values are 2 and 4, since each is a power of two greater than 1 and reaches 1 after one popcount.

#### Example 2

- **Input:** `n = 7, k = 2`
- **Output:** `3`
- **Explanation:** Values 3, 5, and 6 each contain two set bits, so their sequence reaches 2 and then 1.

#### Example 3

- **Input:** `n = 1, k = 0`
- **Output:** `1`
- **Explanation:** The initial value is already 1, so its depth is zero.
