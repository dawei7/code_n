# Minimum Numbers of Function Calls to Make Target Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1558 |
| Difficulty | Medium |
| Topics | Array, Greedy, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/) |

## Problem Description
### Goal

You are given a target integer array `nums`. Begin with an array `arr` of the same length whose entries are all zero. One call may either increment one chosen entry of `arr` by one or double every entry of `arr` simultaneously.

Apply these calls until `arr` equals `nums`, and return the minimum possible number of calls. Target entries may be zero, and the test data guarantees that the answer fits in a signed 32-bit integer.

### Function Contract
**Inputs**

- `nums`: An array of $N$ integers, where $1 \le N \le 10^5$ and every value lies in $[0,10^9]$.
- Let $B$ be the maximum bit length among the values, with $B=0$ when every value is zero. The source bound gives $0 \le B \le 30$.

**Return value**

Return the fewest permitted function calls required to transform the all-zero array into `nums`.

### Examples
**Example 1**

- Input: `nums = [1,5]`
- Output: `5`

**Example 2**

- Input: `nums = [2,2]`
- Output: `3`

**Example 3**

- Input: `nums = [4,2,5]`
- Output: `6`
