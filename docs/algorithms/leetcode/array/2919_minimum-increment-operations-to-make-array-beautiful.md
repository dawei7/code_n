# Minimum Increment Operations to Make Array Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2919 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [minimum-increment-operations-to-make-array-beautiful](https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers and a threshold `k`, determine the minimum total increment operations required such that every contiguous subarray of length 3 contains at least one element greater than or equal to `k`. An increment operation consists of increasing any element in the array by 1.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.
- `k`: An integer representing the minimum threshold value.

**Return value**

- An integer representing the minimum total increments needed to satisfy the condition.

### Examples
**Example 1**

- Input: `nums = [2, 3, 0, 0, 2], k = 4`
- Output: `3`

**Example 2**

- Input: `nums = [0, 1, 3, 3], k = 5`
- Output: `2`

**Example 3**

- Input: `nums = [1, 1, 2], k = 1`
- Output: `0`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain a state representing the minimum cost to satisfy the condition up to index `i`, considering the "distance" to the last element that was made $\ge k$. Specifically, we track the minimum cost to have the last element $\ge k$ at index `i`, `i-1`, or `i-2`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array once with constant time transitions.
- **Space Complexity**: `O(1)`, as we only store the costs for the last three positions.
