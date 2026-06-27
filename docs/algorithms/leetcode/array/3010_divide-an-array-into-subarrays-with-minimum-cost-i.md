# Divide an Array Into Subarrays With Minimum Cost I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3010 |
| Difficulty | Easy |
| Topics | Array, Sorting, Enumeration |
| Official Link | [divide-an-array-into-subarrays-with-minimum-cost-i](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, partition the array into exactly three contiguous subarrays such that the sum of the first elements of each subarray is minimized. The first subarray must always start at the first index of the array.

### Function Contract
**Inputs**

- `nums`: A list of integers where `nums.length >= 3`.

**Return value**

- An integer representing the minimum possible sum of the first elements of the three subarrays.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 12]`
- Output: `6`
- Explanation: The subarrays are [1], [2], [3, 12]. The first elements are 1, 2, and 3. Sum = 1 + 2 + 3 = 6.

**Example 2**

- Input: `nums = [5, 4, 3]`
- Output: `12`
- Explanation: The subarrays are [5], [4], [3]. The first elements are 5, 4, and 3. Sum = 5 + 4 + 3 = 12.

**Example 3**

- Input: `nums = [10, 3, 1, 2]`
- Output: `14`
- Explanation: The subarrays are [10], [3], [1, 2]. The first elements are 10, 3, and 1. Sum = 10 + 3 + 1 = 14.

---

## Underlying Base Algorithm(s)
The problem requires the first element of the first subarray to be `nums[0]`. To minimize the total sum, we must select the two smallest values from the remaining portion of the array (`nums[1:]`) to serve as the starting elements of the second and third subarrays. This is achieved by sorting the suffix or using a linear scan to find the two smallest elements.

---

## Complexity Analysis
- **Time Complexity**: O(N log N) due to sorting, or O(N) if using a linear scan to find the two smallest elements.
- **Space Complexity**: O(1) if sorting in-place or O(N) depending on the sorting implementation.
