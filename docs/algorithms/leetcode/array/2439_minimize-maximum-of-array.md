# Minimize Maximum of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2439 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming, Greedy, Prefix Sum |
| Official Link | [minimize-maximum-of-array](https://leetcode.com/problems/minimize-maximum-of-array/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers, you are permitted to perform an operation any number of times: choose an index `i` (where `i > 0`) and decrease `nums[i]` by 1 while increasing `nums[i-1]` by 1. The objective is to minimize the maximum value present in the array after performing any number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the smallest possible maximum value of the array after optimal operations.

### Examples
**Example 1**

- Input: `nums = [3, 7, 1, 6]`
- Output: `5`
- Explanation: Move 1 from index 1 to 0, then 1 from index 3 to 2, etc., to balance the values.

**Example 2**

- Input: `nums = [10, 1]`
- Output: `10`
- Explanation: We can only move values from right to left. Since index 0 cannot pass values to the left, the value at index 0 remains 10.

**Example 3**

- Input: `nums = [13, 13, 13, 13]`
- Output: `13`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Prefix Sum** approach. Since operations only allow moving values from index `i` to `i-1`, any value at index `i` can eventually contribute to the average of all elements from index `0` to `i`. The maximum value in the array will be at least the ceiling of the prefix average at any point `i`. By iterating through the array and maintaining a running prefix sum, we calculate `ceil(prefix_sum / (i + 1))` and track the maximum of these values.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass through the array.
- **Space Complexity**: `O(1)`, as we only store a few variables for the running sum and the maximum result.
