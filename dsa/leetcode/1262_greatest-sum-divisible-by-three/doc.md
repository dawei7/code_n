# Greatest Sum Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1262 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/greatest-sum-divisible-by-three/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Select any subset of its elements and add the selected values. Each array position may be used at most once, and the selection does not need to be contiguous.

Return the largest achievable sum that is divisible by $3$. Selecting no elements is allowed, so zero is always a valid candidate when no positive divisible sum can be formed.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 4\cdot10^4$ and $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the maximum subset sum whose remainder modulo $3$ is zero.

### Examples

**Example 1**

- Input: `nums = [3, 6, 5, 1, 8]`
- Output: `18`
- Explanation: Selecting `3`, `6`, `1`, and `8` gives the largest divisible sum.

**Example 2**

- Input: `nums = [4]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 4]`
- Output: `12`
