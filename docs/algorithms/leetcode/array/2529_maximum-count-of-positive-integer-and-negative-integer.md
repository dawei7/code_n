# Maximum Count of Positive Integer and Negative Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2529 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Counting |
| Official Link | [maximum-count-of-positive-integer-and-negative-integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/) |

## Problem Description & Examples
### Goal
Given a sorted array of integers, determine the count of strictly positive integers and strictly negative integers. Return the larger of these two counts.

### Function Contract
**Inputs**

- `nums`: A list of integers sorted in non-decreasing order.

**Return value**

- An integer representing the maximum of the count of positive numbers and the count of negative numbers.

### Examples
**Example 1**

- Input: `nums = [-2, -1, -1, 1, 2, 3]`
- Output: `3`

**Example 2**

- Input: `nums = [-3, -2, -1, 0, 0, 1, 2]`
- Output: `3`

**Example 3**

- Input: `nums = [5, 20, 66, 1314]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Binary Search. Since the array is sorted, we can use binary search (specifically `bisect_left` and `bisect_right`) to find the boundaries where negative numbers end and positive numbers begin in $O(\log n)$ time.

---

## Complexity Analysis
- **Time Complexity**: $O(\log n)$, where $n$ is the length of the array, due to the use of binary search to locate the split points.
- **Space Complexity**: $O(1)$, as we only store a few integer variables regardless of the input size.
