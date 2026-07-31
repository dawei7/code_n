# Find the Maximum Length of a Good Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3177 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/) |

## Problem Description
### Goal
You are given an integer array `nums` and a non-negative integer `k`. A sequence `seq` is good if there are at most $k$ indices $i$ from $0$ through `seq.length - 2` at which two adjacent sequence values differ: `seq[i] != seq[i + 1]`.

Select a subsequence of `nums` while preserving the relative order of its chosen elements. Return the maximum possible length among all good subsequences. Only adjacency inside the selected subsequence matters, so omitted array elements do not contribute changes.

### Function Contract
**Inputs**

- `nums`: A list of $n$ positive integers from which a subsequence may be selected.
- `k`: The maximum number of unequal adjacent selected pairs allowed in the subsequence.

The constraints are $1 \le n \le 5000$, $1 \le \texttt{nums[i]} \le 10^9$, and $0 \le k \le \min(50,n)$.

**Return value**

Return the maximum length of a subsequence containing at most $k$ adjacent value changes.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 1, 3], k = 2`
- Output: `4`

One maximum-length choice is `[1, 2, 1, 1]`, whose adjacent selected values change twice.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 1], k = 0`
- Output: `2`

Selecting the first and last elements produces `[1, 1]`, so no adjacent selected values differ.
