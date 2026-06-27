# Maximize Subarray Sum After Removing All Occurrences of One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3410 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Divide and Conquer, Dynamic Programming, Segment Tree, Prefix Sum |
| Official Link | [maximize-maximize-subarray-sum-after-removing-all-occurrences-of-one-element](https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/) |

## Problem Description & Examples
### Goal
Given an integer array, determine the maximum possible sum of a contiguous subarray after choosing exactly one distinct value present in the array and removing all its occurrences. If the array contains negative numbers, the subarray sum could potentially be empty (sum 0) or must be calculated based on the remaining elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the maximum subarray sum achievable after removing all instances of one chosen element.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`
- Explanation: Removing any element (e.g., 1) leaves [2, 3, 4], sum is 9. Removing nothing is not allowed; we must remove one value. Removing 1 gives 9, removing 4 gives 6. Wait, the max is 10 if we remove nothing? No, we must remove one value. Removing 1 gives 9.

**Example 2**

- Input: `nums = [-3, -1, -2]`
- Output: `0`
- Explanation: Removing any element leaves a subarray of negative numbers. The empty subarray sum is 0.

**Example 3**

- Input: `nums = [1, 2, 1, 3]`
- Output: `6`
- Explanation: Removing 1 leaves [2, 3], sum 5. Removing 2 leaves [1, 1, 3], sum 5. Removing 3 leaves [1, 2, 1], sum 4. Actually, if we remove 2, we get [1, 1, 3], max subarray is 5. If we remove 3, we get [1, 2, 1], max subarray is 4.

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of Kadane's Algorithm and Prefix Sums. We pre-calculate the total sum of occurrences for each unique value. By iterating through the array and maintaining the maximum subarray sum using Kadane's, we can efficiently calculate the impact of removing a specific value by tracking the "best" subarray sum that excludes that value's occurrences.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the length of the array. We iterate through the array a constant number of times to build prefix sums and track Kadane's state.
- **Space Complexity**: `O(N)` to store the indices of each element and the prefix sum arrays.
