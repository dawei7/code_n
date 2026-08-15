# Partition Array Into K-Distinct Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3659 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-into-k-distinct-groups/) |

## Problem Description

### Goal

Given an integer array `nums` and an integer `k`, decide whether every array element can be assigned to a collection of one or more groups. Every occurrence must be used exactly once, including repeated occurrences of the same value.

Each group must contain exactly `k` elements. Within any single group, all `k` values must be distinct; equal values may still appear in different groups.

Return `true` when such a complete partition exists. Return `false` when the array length, value multiplicities, or both make the required grouping impossible. The order of elements inside groups is irrelevant.

### Function Contract

**Inputs**

- `nums`: a nonempty integer array of length $n$, where $1\le n\le 10^5$ and $1\le\texttt{nums[i]}\le 10^5$.
- `k`: the exact size of every group, where $1\le k\le n$.

**Return value**

Return a Boolean indicating whether all occurrences can be partitioned into size-`k` groups whose elements are pairwise distinct within each group.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4]`, `k = 2`
- **Output:** `true`
- One partition is `[1, 2]` and `[3, 4]`.

#### Example 2

- **Input:** `nums = [3, 5, 2, 2]`, `k = 2`
- **Output:** `true`
- The two copies of `2` can be separated into `[2, 3]` and `[2, 5]`.

#### Example 3

- **Input:** `nums = [1, 5, 2, 3]`, `k = 3`
- **Output:** `false`
- Four elements cannot be divided into groups containing exactly three elements each.
