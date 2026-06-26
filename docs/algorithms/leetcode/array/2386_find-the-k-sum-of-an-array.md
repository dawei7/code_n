# Find the K-Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2386 |
| Difficulty | Hard |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Official Link | [find-the-k-sum-of-an-array](https://leetcode.com/problems/find-the-k-sum-of-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, calculate the k-th largest subsequence sum. A subsequence is formed by deleting zero or more elements from the original array. Note that the empty subsequence has a sum of 0.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the rank of the subsequence sum to find.

**Return value**

- An integer representing the k-th largest subsequence sum.

### Examples
**Example 1**

- Input: `nums = [2, 4, -2], k = 5`
- Output: `2`
- Explanation: The subsequence sums are: [4, 2, 2, 2, 0, 0, -2, -2]. The 5th largest is 2.

**Example 2**

- Input: `nums = [1, -2, 3, 4, -10, 12], k = 16`
- Output: `10`

**Example 3**

- Input: `nums = [10, -2, 10], k = 1`
- Output: `20`

---

## Underlying Base Algorithm(s)
The problem is solved by first calculating the maximum possible subsequence sum (the sum of all positive numbers). To find the subsequent k-1 sums, we treat the problem as finding the smallest "losses" from the maximum sum. We transform the array by taking the absolute values of all elements and sorting them. We then use a min-heap to explore combinations of these absolute values, which represent the subtractions from the maximum sum.

---

## Complexity Analysis
- **Time Complexity**: O(n log n + k log k), where n is the length of the array. Sorting takes O(n log n), and extracting k elements from the heap takes O(k log k).
- **Space Complexity**: O(n + k), to store the sorted array and the heap elements.
