# Find the Value of the Partition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2740 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-the-value-of-the-partition/) |

## Problem Description

### Goal

Given a positive integer array `nums`, distribute every element into exactly one of two arrays, `nums1` and `nums2`. Both resulting arrays must contain at least one element.

The value of a partition is the absolute difference between the largest element placed in `nums1` and the smallest element placed in `nums2`, namely `abs(max(nums1) - min(nums2))`. Choose the distribution that makes this value as small as possible and return that minimum. The original order of `nums` does not constrain either group.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: An array of positive integers, where $2 \le n \le 10^5$ and $1 \le \texttt{nums}[i] \le 10^9$.

**Return value**

Return the minimum possible value of `abs(max(nums1) - min(nums2))` over all assignments of the elements to two non-empty arrays.

### Examples

**Example 1**

- Input: `nums = [1,3,2,4]`
- Output: `1`
- Explanation: Choosing `nums1 = [1,2]` and `nums2 = [3,4]` gives `abs(2 - 3) = 1`, which is minimal.

**Example 2**

- Input: `nums = [100,1,10]`
- Output: `9`
- Explanation: Choosing `nums1 = [10]` and `nums2 = [100,1]` gives `abs(10 - 1) = 9`.

**Example 3**

- Input: `nums = [5,3,5,9]`
- Output: `0`
- Explanation: Put one occurrence of `5` in each array so the relevant maximum and minimum are equal.
