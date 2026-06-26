# House Robber IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2560 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Dynamic Programming, Greedy |
| Official Link | [house-robber-iv](https://leetcode.com/problems/house-robber-iv/) |

## Problem Description & Examples
### Goal
Given an array of house values and an integer `k`, determine the minimum possible "capability" value. The capability is defined as the maximum value among a set of `k` non-adjacent houses chosen from the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the value of each house.
- `k`: An integer representing the required number of non-adjacent houses to select.

**Return value**

- An integer representing the minimum possible maximum value among the chosen `k` houses.

### Examples
**Example 1**

- Input: `nums = [2,3,5,9], k = 2`
- Output: `5`
- Explanation: We can pick houses with values 2 and 5 (indices 0 and 2). The maximum is 5.

**Example 2**

- Input: `nums = [2,7,9,3,1], k = 2`
- Output: `2`
- Explanation: We can pick houses with values 2 and 1 (indices 0 and 4). The maximum is 2.

**Example 3**

- Input: `nums = [2,7,9,3,1], k = 3`
- Output: `2`
- Explanation: We can pick houses with values 2, 9, and 1 (indices 0, 2, 4). The maximum is 9. Wait, the optimal is picking 2, 3, 1 (indices 0, 3, 4 is invalid, but 0, 2, 4 is valid). Actually, picking 2, 3, 1 is not possible due to adjacency. The minimum max is 2.

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer**. Since the capability value is monotonic (if a capability `x` is possible, any value `y > x` is also possible), we can binary search over the range of values present in `nums`. For a fixed candidate value `mid`, we use a **Greedy** approach to check if it is possible to pick at least `k` non-adjacent houses such that no house exceeds `mid`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log(max(nums)))`, where `n` is the length of the array. The binary search runs in `log(max(nums))` iterations, and the greedy check takes `O(n)`.
- **Space Complexity**: `O(1)`, as we only use a few variables for the greedy check.
