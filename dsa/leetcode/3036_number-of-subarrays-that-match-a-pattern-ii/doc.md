# Number of Subarrays That Match a Pattern II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3036 |
| Difficulty | Hard |
| Topics | Array, Rolling Hash, String Matching, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/) |

## Problem Description
### Goal
You are given a 0-indexed integer array `nums` of length $n$ and a 0-indexed array `pattern` of length $m$. Every entry of `pattern` is `-1`, `0`, or `1`.

A contiguous subarray `nums[i..i + m]` has length $m+1$. It matches `pattern` when each adjacent pair has the relation requested at the corresponding pattern index $k$: the next number is strictly greater when `pattern[k] == 1`, equal when `pattern[k] == 0`, and strictly smaller when `pattern[k] == -1`.

Return the number of length-$(m+1)$ subarrays that satisfy all $m$ relations. Distinct starting positions count separately, so matching subarrays may overlap.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$ and $m=\lvert\texttt{pattern}\rvert$.

**Inputs**

- `nums`: An integer array with $2 \le n \le 10^6$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `pattern`: An array of length $1 \le m<n$ whose entries belong to $\{-1,0,1\}$.

**Return value**

Return the number of starting indices whose next $m$ adjacent comparisons match `pattern` in order.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5,6], pattern = [1,1]`
- Output: `4`
- Explanation: Each of the four length-three subarrays is strictly increasing, so each realizes `[1,1]`.

**Example 2**

- Input: `nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]`
- Output: `2`
- Explanation: `[1,4,4,1]` and `[3,5,5,3]` each increase, stay equal, and then decrease.
