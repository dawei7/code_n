# Smallest Subarrays With Maximum Bitwise OR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2411 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) |

## Problem Description

### Goal

For every index $i$ in a 0-indexed array of non-negative integers, consider all non-empty subarrays that start at $i$. Their right endpoint may be any $j$ from $i$ through the final index. Let $B_{i,j}$ be the bitwise OR of `nums[i...j]`; extending the subarray can add set bits but can never remove them.

Find the minimum length of a subarray starting at each $i$ whose OR equals the maximum possible value $\max_{i \le k < n} B_{i,k}$. Return all $n$ lengths in index order. The chosen sequence must be a contiguous subarray, and length 1 is valid when `nums[i]` already contains every bit available in its suffix.

### Function Contract

**Inputs**

- `nums`: A non-empty array of non-negative integers.

Let $n = \lvert\texttt{nums}\rvert$. The contract guarantees $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^9$, so only bit positions 0 through 29 can be set.

**Return value**

Return an array `answer` of length $n$, where `answer[i]` is the smallest positive length whose subarray starting at $i$ reaches that start's maximum possible bitwise OR.

### Examples

**Example 1**

- Input: `nums = [1,0,2,1,3]`
- Output: `[3,3,2,2,1]`

**Example 2**

- Input: `nums = [1,2]`
- Output: `[2,1]`

**Example 3**

- Input: `nums = [0,0]`
- Output: `[1,1]`
