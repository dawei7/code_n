# Count of Range Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 327 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Official Link | [count-of-range-sum](https://leetcode.com/problems/count-of-range-sum/) |

## Problem Description & Examples
### Goal
Given an integer array and two bounds, determine the total number of contiguous subarrays whose sum falls within the inclusive range `[lower, upper]`. A subarray is defined as a contiguous sequence of elements within the array.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `lower`: An integer representing the lower bound of the sum.
- `upper`: An integer representing the upper bound of the sum.

**Return value**

- An integer representing the count of subarrays where `lower <= sum(subarray) <= upper`.

### Examples
**Example 1**

- Input: `nums = [-2, 5, -1], lower = -2, upper = 2`
- Output: `3`
- Explanation: The valid subarrays are `[-2]`, `[-1]`, and `[-2, 5, -1]`, with sums `-2`, `-1`, and `2` respectively.

**Example 2**

- Input: `nums = [0], lower = 0, upper = 0`
- Output: `1`

**Example 3**

- Input: `nums = [1], lower = 0, upper = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Merge Sort** technique applied to prefix sums. By calculating prefix sums, the sum of a subarray `nums[i:j]` is equivalent to `prefix_sum[j] - prefix_sum[i]`. The condition `lower <= prefix_sum[j] - prefix_sum[i] <= upper` can be rearranged to `prefix_sum[j] - upper <= prefix_sum[i] <= prefix_sum[j] - lower`. During the merge step of the sort, we count pairs that satisfy this inequality in linear time, resulting in an efficient divide-and-conquer approach.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the input array. The merge sort process divides the array into halves recursively, and the counting step at each level takes linear time.
- **Space Complexity**: `O(n)` to store the prefix sums and the auxiliary array used during the merge sort process.
