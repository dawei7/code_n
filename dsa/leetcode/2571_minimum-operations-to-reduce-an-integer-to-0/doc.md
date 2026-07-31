# Minimum Operations to Reduce an Integer to 0

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2571 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Operations to Reduce an Integer to 0](https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/) |

## Problem Description

### Goal

You are given a positive integer `n`. In one operation, choose any nonnegative integer $i$ and either add or subtract $2^i$ from the current value. The chosen power of two may be different in each operation, and intermediate values are allowed to be larger than the original input.

Return the minimum number of operations needed to make the value equal to zero.

### Function Contract

**Inputs**

- `n`: A positive integer satisfying $1 \le n \le 10^5$.

**Return value**

Return an integer equal to the fewest permitted additions and subtractions required to reach zero.

### Examples

**Example 1**

- Input: `n = 39`
- Output: `3`
- Explanation: Add $1$ to obtain `40`, subtract $8$ to obtain `32`, and subtract $32$ to obtain `0`.

**Example 2**

- Input: `n = 54`
- Output: `3`
- Explanation: Add $2$ to obtain `56`, add $8$ to obtain `64`, and subtract $64$ to obtain `0`.

**Example 3**

- Input: `n = 28`
- Output: `2`
- Explanation: Adding $4$ carries through the adjacent set bits and produces `32`, which can then be reduced to zero in one subtraction.
