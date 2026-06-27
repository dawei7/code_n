# Minimum Absolute Difference Between Elements With Constraint

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2817 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Ordered Set |
| Official Link | [minimum-absolute-difference-between-elements-with-constraint](https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/) |

## Problem Description & Examples
### Goal
Given an array of integers and a non-negative integer `x`, find the minimum absolute difference between any two elements `nums[i]` and `nums[j]` such that the absolute difference between their indices `i` and `j` is at least `x`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `x`: An integer representing the minimum required index distance.

**Return value**

- An integer representing the minimum absolute difference found between any two elements satisfying the index constraint.

### Examples
**Example 1**

- Input: `nums = [4,3,2,4], x = 2`
- Output: `0`
- Explanation: We can choose indices 0 and 3. |4 - 4| = 0, and |0 - 3| = 3 >= 2.

**Example 2**

- Input: `nums = [5,3,2,10,15], x = 1`
- Output: `1`
- Explanation: We can choose indices 1 and 2. |3 - 2| = 1, and |1 - 2| = 1 >= 1.

**Example 3**

- Input: `nums = [1,2,3,4], x = 3`
- Output: `3`
- Explanation: We can choose indices 0 and 3. |1 - 4| = 3, and |0 - 3| = 3 >= 3.

---

## Underlying Base Algorithm(s)
The problem is solved using a sliding window approach combined with a balanced binary search tree (or a sorted list). As we iterate through the array with index `i`, we maintain a collection of elements that satisfy the index constraint (i.e., elements at indices `0` to `i - x`). By using `bisect_left` on a sorted list, we can efficiently find the elements closest in value to `nums[i]` to calculate the minimum absolute difference.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`, where `n` is the length of the array. We iterate through the array once, and for each element, we perform insertion and binary search in a sorted list, both taking `O(log n)` time.
- **Space Complexity**: `O(n)` to store the elements in the sorted list.
