# Partition Array into Disjoint Intervals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 915 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) |

## Problem Description
### Goal

Given an integer array `nums`, divide it at one boundary into two contiguous subarrays named `left` and `right`. Both subarrays must be non-empty, and every element in `left` must be less than or equal to every element in `right`.

Among all boundaries satisfying that ordering condition, choose the one that gives `left` the smallest possible size. Return the length of `left`. The input is guaranteed to admit at least one valid partition.

### Function Contract
**Inputs**

- `nums`: an array of $n$ integers, where $2 \le n \le 10^5$ and $0 \le \textit{nums}[i] \le 10^6$.

**Return value**

The smallest index count $k$, with $1 \le k<n$, such that every value in `nums[:k]` is less than or equal to every value in `nums[k:]`.

### Examples
**Example 1**

- Input: `nums = [5,0,3,8,6]`
- Output: `3`
- Explanation: `left = [5,0,3]` and `right = [8,6]`.

**Example 2**

- Input: `nums = [1,1,1,0,6,12]`
- Output: `4`
- Explanation: The zero forces the first four values into `left`.

**Example 3**

- Input: `nums = [1,2]`
- Output: `1`
- Explanation: The first element alone already satisfies the condition.
