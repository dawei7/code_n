# Least Number of Unique Integers after K Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1481 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) |

## Problem Description
### Goal

Given an integer array `arr` and an integer `k`, remove exactly `k` array elements. Each removal chooses one occurrence, so deleting some—but not all—copies of a value does not remove that value from the set of integers still present.

After all removals, minimize the number of unique integers represented by the remaining elements. Return that minimum count. The array may become empty when `k` equals its length.

### Function Contract
**Inputs**

Let $N$ be the length of `arr`, and let $U$ be the number of distinct values in it.

- `arr`: an integer array with $1 \le N \le 10^5$.
- Every element satisfies $1 \le \texttt{arr[i]} \le 10^9$.
- `k`: the exact number of elements to remove, with $0 \le k \le N$.

**Return value**

Return the least possible number of distinct integers remaining after exactly `k` occurrence removals.

### Examples
**Example 1**

- Input: `arr = [5,5,4], k = 1`
- Output: `1`
- Explanation: Removing the only `4` eliminates that value completely, leaving only `5`.

**Example 2**

- Input: `arr = [4,3,1,1,3,3,2], k = 3`
- Output: `2`
- Explanation: Remove the singleton values `4` and `2`, then remove one occurrence of either remaining value. Both `1` and `3` are still represented.
