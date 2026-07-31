# Find the Longest Equal Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2831 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-longest-equal-subarray/) |

## Problem Description
### Goal

You are given a 0-indexed integer array `nums` and an integer `k`. A subarray is equal when every element in it has the same value; the empty subarray also satisfies this definition.

You may delete at most `k` elements from `nums`. Deletions close the resulting gaps, so equal values that were separated in the original array can become contiguous. Elements outside the chosen equal subarray do not need to be deleted.

Return the length of the longest equal subarray that can exist after the permitted deletions. A subarray is a contiguous, possibly empty sequence in the resulting array.

### Function Contract
**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le n$.
- `k`: The maximum number of deletions, where $0 \le k \le n$.

**Return value**

Return the greatest number of equal elements that can be made contiguous after deleting at most `k` array elements.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 3, 1, 3], k = 3`
- Output: `3`
- Explanation: Delete the values at indices `2` and `4`. The three occurrences of `3` become consecutive, producing an equal subarray of length `3`.

**Example 2**

- Input: `nums = [1, 1, 2, 2, 1, 1], k = 2`
- Output: `4`
- Explanation: Removing the two middle occurrences of `2` joins all four occurrences of `1` into one equal subarray.
