# Number of Subarrays That Match a Pattern I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3034 |
| Difficulty | Medium |
| Topics | Array, Rolling Hash, String Matching, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/) |

## Problem Description
### Goal
You are given a 0-indexed integer array `nums` of length $n$ and a 0-indexed array `pattern` of length $m$. Every pattern value is one of `-1`, `0`, or `1`.

A contiguous subarray `nums[i..i + m]` has the required length $m+1$. It matches `pattern` when every adjacent pair expresses the relation specified at the corresponding pattern index $k$: the next value must be strictly greater when `pattern[k] == 1`, equal when `pattern[k] == 0`, and strictly smaller when `pattern[k] == -1`.

Return the number of length-$(m+1)$ subarrays of `nums` that satisfy all $m$ relations. Overlapping matching subarrays are counted separately.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$, let $m=\lvert\texttt{pattern}\rvert$, and let $W=n-m$ be the number of candidate starting positions.

**Inputs**

- `nums`: An integer array with $2 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `pattern`: An array of length $1 \le m<n$ whose entries lie in $\{-1,0,1\}$.

**Return value**

Return the count of candidate subarrays whose adjacent comparisons match every entry of `pattern` in order.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5,6], pattern = [1,1]`
- Output: `4`
- Explanation: The four length-three subarrays are all strictly increasing, so each realizes the two relations `[1,1]`.

**Example 2**

- Input: `nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]`
- Output: `2`
- Explanation: `[1,4,4,1]` and `[3,5,5,3]` each increase, remain equal, and then decrease.
