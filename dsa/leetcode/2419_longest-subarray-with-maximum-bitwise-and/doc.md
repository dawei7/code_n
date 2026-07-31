# Longest Subarray With Maximum Bitwise AND

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2419 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) |

## Problem Description

### Goal

Consider every non-empty contiguous subarray of the positive integer array `nums`. Each subarray has a value equal to the bitwise AND of all its elements. Let $k$ be the greatest such value obtainable by any subarray.

Among only the subarrays whose bitwise AND equals $k$, return the maximum length. A single element is a valid subarray, while equal maximum values separated by any smaller value belong to different runs and cannot be joined without changing the AND.

### Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers.

Let $n = \lvert\texttt{nums}\rvert$. The contract guarantees $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

Return the length of the longest contiguous subarray attaining the maximum possible bitwise AND.

### Examples

**Example 1**

- Input: `nums = [1,2,3,3,2,2]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `1`

**Example 3**

- Input: `nums = [7,7,7,7]`
- Output: `4`
