# The kth Factor of n

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1492 |
| Difficulty | Medium |
| Topics | Math, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/) |

## Problem Description
### Goal

For positive integers $n$ and $k$, call a positive integer $d$ a factor of $n$ when $n$ is divisible by $d$ with no remainder. Arrange every positive factor of $n$ in strictly increasing order.

Return the factor at one-based position $k$ in that ordering. If $n$ has fewer than $k$ positive factors, return `-1`. The required method should exploit paired divisors and run in less than $O(n)$ time.

### Function Contract
**Inputs**

- `n`: a positive integer with $1 \le n \le 1000$.
- `k`: a one-based rank satisfying $1 \le k \le n$.

**Return value**

Return the $k$-th smallest positive factor of $n$. Return `-1` when no factor occupies that rank.

### Examples
**Example 1**

- Input: `n = 12, k = 3`
- Output: `3`
- Explanation: The ordered factors are `[1,2,3,4,6,12]`, so the third is `3`.

**Example 2**

- Input: `n = 7, k = 2`
- Output: `7`
- Explanation: A prime number has factors `1` and itself.

**Example 3**

- Input: `n = 4, k = 4`
- Output: `-1`
- Explanation: Only `1`, `2`, and `4` divide `4`, so a fourth factor does not exist.
