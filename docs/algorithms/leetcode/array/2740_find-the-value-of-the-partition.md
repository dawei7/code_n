# Find the Value of the Partition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2740 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [find-the-value-of-the-partition](https://leetcode.com/problems/find-the-value-of-the-partition/) |

## Problem Description & Examples
### Goal
Given an array of positive integers `nums`, your task is to partition it into two non-empty arrays, `nums1` and `nums2`, such that:
1. Every element of `nums` belongs to either `nums1` or `nums2`.
2. The value of the partition is minimized.

The value of the partition is defined as the absolute difference between the maximum element of `nums1` and the minimum element of `nums2` (i.e., `|max(nums1) - min(nums2)|`), under the condition that all elements in `nums1` are less than or equal to all elements in `nums2`.

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of positive integers containing at least 2 elements.

**Return value**

- `int` - The minimum possible value of the partition.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 4]`
- Output: `1`
- Explanation: We can partition `nums` into `nums1 = [1, 2]` and `nums2 = [3, 4]`. The maximum of `nums1` is `2` and the minimum of `nums2` is `3`. The value of the partition is `|2 - 3| = 1`, which is the minimum possible.

**Example 2**

- Input: `nums = [100, 1, 10]`
- Output: `9`
- Explanation: We can partition `nums` into `nums1 = [1]` and `nums2 = [10, 100]`. The maximum of `nums1` is `1` and the minimum of `nums2` is `10`. The value of the partition is `|1 - 10| = 9`, which is the minimum possible.

---

## Underlying Base Algorithm(s)
To minimize the partition value `|max(nums1) - min(nums2)|` where all elements in `nums1` are less than or equal to all elements in `nums2`, we can visualize the sorted version of the array. 

If we sort `nums` in ascending order: $a_1 \le a_2 \le \dots \le a_n$, any valid partition that satisfies the condition will split the sorted array at some index $i$ such that:
- $nums1 = \{a_1, a_2, \dots, a_i\}$
- $nums2 = \{a_{i+1}, \dots, a_n\}$

For this partition, $\max(nums1) = a_i$ and $\min(nums2) = a_{i+1}$. The partition value is simply the difference between these two adjacent elements: $a_{i+1} - a_i$.

Thus, the problem reduces to finding the minimum difference between any two adjacent elements in the sorted array.

1. **Sort** the array in non-decreasing order.
2. **Iterate** through the sorted array to find the minimum difference between consecutive elements: `nums[i] - nums[i - 1]`.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log N)$ where $N$ is the length of the array `nums`. This is dominated by the sorting step. The subsequent linear scan takes $\mathcal{O}(N)$ time.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space if we sort the array in-place (or $\mathcal{O}(N)$ depending on the implementation of the sorting algorithm, such as Timsort in Python which requires $\mathcal{O}(N)$ space in the worst case).
