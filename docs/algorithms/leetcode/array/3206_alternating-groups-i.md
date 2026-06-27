# Alternating Groups I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3206 |
| Difficulty | Easy |
| Topics | Array, Sliding Window |
| Official Link | [alternating-groups-i](https://leetcode.com/problems/alternating-groups-i/) |

## Problem Description & Examples
### Goal
Given a circular array of binary values (0s and 1s), identify the number of "alternating groups" of size 3. An alternating group is defined as a triplet of consecutive elements where the middle element differs from both its left and right neighbors (i.e., the pattern is either `0, 1, 0` or `1, 0, 1`).

### Function Contract
**Inputs**

- `colors`: A list of integers where each element is either 0 or 1.

**Return value**

- An integer representing the total count of triplets `(colors[i-1], colors[i], colors[i+1])` that satisfy the alternating condition, accounting for the circular nature of the array.

### Examples
**Example 1**

- Input: `colors = [1, 1, 1]`
- Output: `0`

**Example 2**

- Input: `colors = [0, 1, 0, 0, 1]`
- Output: `3`

**Example 3**

- Input: `colors = [1, 0, 1, 0, 1]`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem utilizes a **Sliding Window** approach with a fixed window size of 3. Because the array is circular, the indices are handled using modulo arithmetic (`i % n`) to ensure that the last elements wrap around to the beginning of the array.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for counters and index tracking.
