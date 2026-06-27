# Minimum Array Length After Pair Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2856 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Greedy, Counting |
| Official Link | [minimum-array-length-after-pair-removals](https://leetcode.com/problems/minimum-array-length-after-pair-removals/) |

## Problem Description & Examples
### Goal
Given a sorted array of integers, you are allowed to repeatedly select two distinct elements from the array and remove them. The objective is to minimize the final length of the array after performing as many such removals as possible.

### Function Contract
**Inputs**

- `nums`: A non-decreasingly sorted list of integers.

**Return value**

- An integer representing the minimum possible length of the array after performing the optimal sequence of removals.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [1, 1, 2, 2, 3, 3]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 1, 2, 2]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem can be solved using a Greedy approach combined with the Pigeonhole Principle. Since the array is sorted, the most frequent element determines the bottleneck. If the count of the most frequent element exceeds half the array length, those excess elements cannot be paired with others, leaving them as the remainder. Otherwise, if the total length is even, we can reduce the array to 0; if odd, we can reduce it to 1.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the length of the array, as we iterate through the array to count frequencies or use a two-pointer approach.
- **Space Complexity**: `O(1)` if using the two-pointer approach on the sorted array, or `O(N)` if using a hash map for frequency counting.
