# Concatenation of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1929 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/concatenation-of-array/) |

## Problem Description
### Goal
An integer array `nums` has length $N$. Construct a new array `ans` of length
$2N$ by placing two copies of `nums` next to each other in the same order.

For every index $i$ with $0 \le i < N$, the first half must satisfy
`ans[i] = nums[i]`, while the corresponding position in the second half must
satisfy `ans[i + N] = nums[i]`. Return the completed array.

### Function Contract
**Inputs**

- `nums`: a list of $N$ integers, where $1 \le N \le 1000$ and every value is
  between $1$ and $1000$, inclusive.

**Return value**

- A list of length $2N$ containing `nums` followed immediately by another copy
  of `nums`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `[1, 2, 1, 1, 2, 1]`

**Example 2**

- Input: `nums = [1, 3, 2, 1]`
- Output: `[1, 3, 2, 1, 1, 3, 2, 1]`

**Example 3**

- Input: `nums = [7]`
- Output: `[7, 7]`
