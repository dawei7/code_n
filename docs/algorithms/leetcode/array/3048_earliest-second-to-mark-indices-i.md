# Earliest Second to Mark Indices I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3048 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [earliest-second-to-mark-indices-i](https://leetcode.com/problems/earliest-second-to-mark-indices-i/) |

## Problem Description & Examples
### Goal
Given an array of target values representing the number of decrements required for each index and a sequence of indices to be marked, determine the earliest second (1-indexed) by which all indices can be marked. At each second, you can either decrement a target value at a specific index or mark an index if its target value has reached zero.

### Function Contract
**Inputs**

- `nums`: A list of integers where `nums[i]` is the number of decrements needed for index `i+1`.
- `changeIndices`: A list of integers representing the index to be potentially marked at each second.

**Return value**

- An integer representing the minimum time (1-indexed) required to mark all indices, or -1 if it is impossible.

### Examples
**Example 1**

- Input: `nums = [2, 2, 0], changeIndices = [2, 2, 2, 2, 3, 2, 2, 1]`
- Output: `8`

**Example 2**

- Input: `nums = [1, 3], changeIndices = [1, 1, 1, 2, 1, 1, 1]`
- Output: `6`

**Example 3**

- Input: `nums = [0, 1], changeIndices = [2, 2, 2, 1]`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem exhibits a monotonic property: if it is possible to mark all indices by time `T`, it is also possible for any time `T' > T`. This allows the use of **Binary Search on the Answer**. For a fixed time `T`, we verify feasibility by greedily processing the `changeIndices` in reverse: we prioritize marking an index as late as possible to maximize the time available for decrements.

---

## Complexity Analysis
- **Time Complexity**: `O(M log M)`, where `M` is the length of `changeIndices`. The binary search runs in `O(log M)` steps, and each check takes `O(M)` time.
- **Space Complexity**: `O(N + M)`, where `N` is the length of `nums` and `M` is the length of `changeIndices`, used to store the last occurrence of each index and the state during the check.
