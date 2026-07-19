# Constrained Subsequence Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1425 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/constrained-subsequence-sum/) |

## Problem Description

### Goal

Choose a nonempty subsequence of `nums` while preserving the original index order. For every pair of consecutive selected elements at indices `i` and `j`, their gap must satisfy $j-i \le k$.

Return the maximum possible sum of such a constrained subsequence. The answer may be negative because at least one element must be selected, and skipping elements does not remove the gap restriction between the selected indices on either side.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.
- `k`: the largest allowed index gap between consecutive selected values, where $1 \le k \le n$.

**Return value**

- The maximum sum of a nonempty subsequence whose consecutive selected indices differ by at most `k`.

### Examples

**Example 1**

- Input: `nums = [10,2,-10,5,20], k = 2`
- Output: `37`

**Example 2**

- Input: `nums = [-1,-2,-3], k = 1`
- Output: `-1`

**Example 3**

- Input: `nums = [10,-2,-10,-5,20], k = 2`
- Output: `23`
