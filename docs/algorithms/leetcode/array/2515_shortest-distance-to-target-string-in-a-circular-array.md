# Shortest Distance to Target String in a Circular Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2515 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [shortest-distance-to-target-string-in-a-circular-array](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/) |

## Problem Description & Examples
### Goal
Given a circular array of strings and a starting index, determine the minimum number of steps required to reach any occurrence of a specified target string. Because the array is circular, movement can occur in either the clockwise or counter-clockwise direction, wrapping around the array boundaries.

### Function Contract
**Inputs**

- `words`: A list of strings representing the circular array.
- `target`: The string to search for within the array.
- `startIndex`: An integer representing the initial position in the array.

**Return value**

- An integer representing the minimum distance (number of steps) to reach the target. If the target does not exist in the array, return -1.

### Examples
**Example 1**

- Input: `words = ["hello", "i", "am", "leetcode", "hello"], target = "hello", startIndex = 1`
- Output: `1`

**Example 2**

- Input: `words = ["a", "b", "leetcode"], target = "leetcode", startIndex = 0`
- Output: `1`

**Example 3**

- Input: `words = ["i", "eat", "apple"], target = "pie", startIndex = 0`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan to identify all indices where the target string exists. Once the indices are found, the shortest distance is calculated by comparing the absolute difference between the `startIndex` and the target index against the circular distance (the total length of the array minus the absolute difference).

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in the `words` array, as we must traverse the array once to find all occurrences of the target.
- **Space Complexity**: O(1), as we only store a few integer variables regardless of the input size.
