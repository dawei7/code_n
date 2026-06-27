# Alternating Groups II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3208 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [alternating-groups-ii](https://leetcode.com/problems/alternating-groups-ii/) |

## Problem Description & Examples
### Goal
Given a circular array of binary values (0s and 1s), identify the total number of contiguous subarrays of a fixed length `k` where the elements alternate between 0 and 1. Because the array is circular, the end of the array wraps around to the beginning.

### Function Contract
**Inputs**

- `colors`: A list of integers (0 or 1) representing the circular sequence.
- `k`: An integer representing the required length of the alternating group.

**Return value**

- An integer representing the count of all contiguous segments of length `k` that satisfy the alternating property.

### Examples
**Example 1**

- Input: `colors = [0, 1, 0, 1, 0], k = 3`
- Output: `3`

**Example 2**

- Input: `colors = [0, 1, 0, 0, 1, 0, 1], k = 6`
- Output: `2`

**Example 3**

- Input: `colors = [1, 1, 0, 1], k = 4`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** approach combined with circular array handling. Since the array is circular, we can conceptually extend the array by appending the first `k-1` elements to the end. We maintain a window of length `k` and track the number of consecutive alternating pairs. If the current element breaks the alternating pattern, the window resets. If the window size reaches `k`, we increment our count.

---

## Complexity Analysis
- **Time Complexity**: `O(n + k)`, where `n` is the length of the `colors` array. We traverse the array once, and the circular extension adds at most `k-1` steps.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track the current window state and the total count, without needing extra data structures proportional to the input size.
