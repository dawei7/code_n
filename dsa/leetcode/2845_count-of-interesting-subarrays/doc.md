# Count of Interesting Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2845 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-interesting-subarrays/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and integers `modulo` and `k`. For a subarray `nums[l..r]`, let `cnt` be the number of indices $i$ from $l$ through $r$ for which `nums[i] % modulo == k`.

The subarray is interesting exactly when `cnt % modulo == k`. Return the total number of interesting subarrays. A subarray must be contiguous and non-empty.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.
- `modulo`: The modulus used for both the element test and the subarray count.
- `k`: The target remainder, satisfying $0\le k<\texttt{modulo}$.

The constraints are $1\le\lvert\texttt{nums}\rvert\le10^5$, $1\le\texttt{nums[i]}\le10^9$, and $1\le\texttt{modulo}\le10^9$. Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- The number of contiguous, non-empty subarrays whose qualifying-element count has remainder `k` modulo `modulo`.

### Examples

**Example 1**

- Input: `nums = [3, 2, 4], modulo = 2, k = 1`
- Output: `3`
- Explanation: `[3]`, `[3, 2]`, and `[3, 2, 4]` each contain one element whose remainder modulo `2` is `1`.

**Example 2**

- Input: `nums = [3, 1, 9, 6], modulo = 3, k = 0`
- Output: `2`
- Explanation: The complete array has three qualifying values, while `[1]` has zero; both counts are divisible by `3`.
