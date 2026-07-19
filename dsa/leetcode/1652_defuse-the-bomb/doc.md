# Defuse the Bomb

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1652 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/defuse-the-bomb/) |

## Problem Description
### Goal
An informer supplies a circular integer array `code` and a key `k`. Decrypt the code by replacing every original element simultaneously. When $k>0$, replace position `i` with the sum of the next $k$ elements. When $k<0$, use the previous $\lvert k\rvert$ elements instead. When $k=0$, replace every position with zero.

The array wraps in both directions: the successor of its final element is the first element, and the predecessor of its first element is the final element. Return all replacement values without letting an earlier replacement affect a later one.

### Function Contract
**Inputs**

- `code`: a circular list of $n$ positive integers, where $1 \le n \le 100$ and $1 \le \texttt{code[i]} \le 100$.
- `k`: the direction and number of neighbors to sum, where $-(n-1) \le k \le n-1$.

**Return value**

Return a list of length $n$ containing every simultaneous replacement.

### Examples
**Example 1**

- Input: `code = [5, 7, 1, 4], k = 3`
- Output: `[12, 10, 16, 13]`

For the first position, the next three values are 7, 1, and 4; later windows wrap around the end.

**Example 2**

- Input: `code = [1, 2, 3, 4], k = 0`
- Output: `[0, 0, 0, 0]`

**Example 3**

- Input: `code = [2, 4, 9, 3], k = -2`
- Output: `[12, 5, 6, 13]`

The first replacement uses the previous two values, 3 and 9.
