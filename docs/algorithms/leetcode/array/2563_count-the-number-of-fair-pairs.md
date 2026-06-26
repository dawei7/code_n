# Count the Number of Fair Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2563 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [count-the-number-of-fair-pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs/) |

## Problem Description & Examples
### Goal
Given an array of integers and two boundary values, identify the total number of index pairs (i, j) such that i < j and the sum of the elements at these indices falls within the inclusive range [lower, upper].

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `lower`: An integer representing the minimum inclusive sum.
- `upper`: An integer representing the maximum inclusive sum.

**Return value**

- An integer representing the count of pairs (i, j) where i < j and lower <= nums[i] + nums[j] <= upper.

### Examples
**Example 1**

- Input: `nums = [0,1,7,4,4,5], lower = 3, upper = 6`
- Output: `6`

**Example 2**

- Input: `nums = [1,7,9,2,5], lower = 11, upper = 11`
- Output: `1`

**Example 3**

- Input: `nums = [1,2,3], lower = 1, upper = 1`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved by sorting the array first, which allows us to use the Two Pointers technique. Since the order of elements does not matter for the sum, sorting enables us to efficiently count pairs that satisfy the condition `sum <= target` by using two pointers moving inward. We calculate the count of pairs with sum <= upper and subtract the count of pairs with sum < lower.

---

## Complexity Analysis
- **Time Complexity**: O(n log n), where n is the length of the array, due to the sorting step. The two-pointer traversal takes O(n).
- **Space Complexity**: O(1) or O(n) depending on the sorting implementation's space requirements (Python's Timsort is O(n)).
