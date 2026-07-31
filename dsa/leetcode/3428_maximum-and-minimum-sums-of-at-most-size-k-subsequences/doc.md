# Maximum and Minimum Sums of at Most Size K Subsequences

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/) |
| Frontend ID | 3428 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Sorting, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You receive an integer array `nums` and a positive integer `k`. Consider every non-empty subsequence whose length is at most `k`. Different choices of indices are different subsequences even when their selected values are equal, and the chosen indices need not be contiguous.

For each such subsequence, add its minimum element and its maximum element. Sum those contributions across all eligible subsequences and return the total modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.
- `k`: The maximum permitted subsequence length.

The constraints are $1 \le n \le 10^5$, $0 \le \texttt{nums[i]} \le 10^9$, and $1 \le k \le \min(70,n)$.

**Return value**

Return the sum of all eligible subsequence minima and maxima modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `nums = [1,2,3], k = 2`
- Output: `24`
- Explanation: The three singleton subsequences contribute `2`, `4`, and `6`; the three size-two subsequences contribute `3`, `4`, and `5`.

**Example 2**

- Input: `nums = [5,0,6], k = 1`
- Output: `22`
- Explanation: Only singletons are eligible, and each value is counted once as both its minimum and maximum.

**Example 3**

- Input: `nums = [1,1,1], k = 2`
- Output: `12`
- Explanation: There are three singleton and three size-two index choices; every one contributes `2`.
