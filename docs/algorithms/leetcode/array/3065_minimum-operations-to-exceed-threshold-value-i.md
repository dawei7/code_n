# Minimum Operations to Exceed Threshold Value I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3065 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [minimum-operations-to-exceed-threshold-value-i](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) |

## Problem Description & Examples
### Goal
Given a collection of integers and a target threshold, determine the minimum number of operations required to ensure that every element in the collection is at least as large as the threshold. An operation consists of removing any single element from the collection.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the current collection.
- `k`: An integer representing the minimum value threshold.

**Return value**

- An integer representing the count of elements that are strictly less than `k`.

### Examples
**Example 1**

- Input: `nums = [2, 11, 10, 1, 3]`, `k = 10`
- Output: `3`

**Example 2**

- Input: `nums = [1, 1, 2, 4, 9]`, `k = 1`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 2, 4, 9]`, `k = 9`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan (filtering). We iterate through the array once and count how many elements fail to meet the condition `x >= k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the input list, as we must inspect each element exactly once.
- **Space Complexity**: `O(1)`, as we only use a single counter variable regardless of the input size.
