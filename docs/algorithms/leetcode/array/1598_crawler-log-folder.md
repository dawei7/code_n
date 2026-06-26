# Crawler Log Folder

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1598 |
| Difficulty | Easy |
| Topics | Array, String, Stack |
| Official Link | [crawler-log-folder](https://leetcode.com/problems/crawler-log-folder/) |

## Problem Description & Examples
### Goal
Given folder navigation logs, determine how many parent-folder moves are needed
to return from the final folder to the main folder.

### Function Contract
**Inputs**

- `logs`: operations of the form `"../"`, `"./"`, or `"name/"`.

**Return value**

The final folder depth relative to the main folder.

### Examples
**Example 1**

- Input: `logs = ["d1/", "d2/", "../", "d21/", "./"]`
- Output: `2`

**Example 2**

- Input: `logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]`
- Output: `3`

**Example 3**

- Input: `logs = ["d1/", "../", "../", "../"]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Track only the current depth. A child-folder operation increments depth,
`"../"` decrements depth if it is positive, and `"./"` leaves it unchanged.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
