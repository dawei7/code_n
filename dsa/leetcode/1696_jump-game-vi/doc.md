# Jump Game VI

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1696 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-vi/) |

## Problem Description
### Goal

You begin at index `0` of the 0-indexed integer array `nums` and must reach index `n - 1`. From index `i`, one move may land at any index from `i + 1` through `min(n - 1, i + k)`, inclusive. Jumps only move forward and may use fewer than $k$ steps.

Your score is the sum of `nums[j]` over every visited index, including the starting and final positions. Values may be negative, so some losses can be unavoidable. Choose the sequence of legal jumps that reaches the last index with the maximum possible score, and return that score.

### Function Contract
**Inputs**

- `nums`: a list of $n$ integers, where $1 \le n \le 10^5$ and each value lies between $-10^4$ and $10^4$
- `k`: the inclusive maximum forward jump length, where $1 \le k \le 10^5$

**Return value**

The greatest score among all legal paths from index `0` to index `n - 1`.

### Examples
**Example 1**

- Input: `nums = [1, -1, -2, 4, -7, 3], k = 2`
- Output: `7`

Visiting values `[1, -1, 4, 3]` achieves the optimum.

**Example 2**

- Input: `nums = [10, -5, -2, 4, 0, 3], k = 3`
- Output: `17`

The path through values `[10, 4, 3]` skips the early negative positions.

**Example 3**

- Input: `nums = [1, -5, -20, 4, -1, 3, -6, -3], k = 2`
- Output: `0`
