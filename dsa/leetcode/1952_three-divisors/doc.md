# Three Divisors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1952 |
| Difficulty | Easy |
| Topics | Math, Enumeration, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/three-divisors/) |

## Problem Description
### Goal
A positive integer $m$ is a divisor of $n$ when some integer $k$ satisfies
$n=km$. Given `n`, determine whether its set of positive divisors contains
exactly three distinct values.

Return `true` only for numbers with exactly three positive divisors, counting
1 and `n` themselves. Return `false` for every other divisor count.
The divisors must be positive, distinct integers and are counted without
multiplicity.

### Function Contract
**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^4$.

**Return value**

- `true` if `n` has exactly three positive divisors; otherwise, `false`.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `false`
- Explanation: Its positive divisors are 1 and 2.

**Example 2**

- Input: `n = 4`
- Output: `true`
- Explanation: Its positive divisors are 1, 2, and 4.

**Example 3**

- Input: `n = 16`
- Output: `false`
- Explanation: Its positive divisors are 1, 2, 4, 8, and 16.
