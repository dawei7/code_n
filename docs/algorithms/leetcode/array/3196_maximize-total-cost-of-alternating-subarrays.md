# Maximize Total Cost of Alternating Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3196 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [maximize-total-cost-of-alternating-subarrays](https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/) |

## Problem Description & Examples
### Goal
Given an array of integers, partition it into contiguous subarrays. For each subarray, calculate its "cost" by alternating the signs of its elements: the first element is added, the second is subtracted, the third is added, and so on. The objective is to maximize the sum of the costs of all these subarrays.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum possible total cost after partitioning the array optimally.

### Examples
**Example 1**

- Input: `nums = [1, -2, 3, 4]`
- Output: `10`
- Explanation: Partition as `[1], [-2], [3, 4]`. Costs: `1 + (-2) + (3 - 4) = -2` (Incorrect). Optimal: `[1], [-2, 3], [4]` -> `1 + (-(-2) + 3) + 4 = 1 + 5 + 4 = 10`.

**Example 2**

- Input: `nums = [1, -1, 1, -1]`
- Output: `4`
- Explanation: Partition as `[1], [-1], [1], [-1]`. Costs: `1 + (-1) + 1 + (-1) = 0` (Incorrect). Optimal: `[1, -1, 1, -1]` -> `1 - (-1) + 1 - (-1) = 4`.

**Example 3**

- Input: `nums = [0]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain two states at each index `i`:
1. `dp0`: The maximum cost ending at index `i` where `nums[i]` is the start of a new subarray (added).
2. `dp1`: The maximum cost ending at index `i` where `nums[i]` is the second (or later) element of a subarray (subtracted).

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only store the previous state values regardless of input size.
