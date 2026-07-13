# Shortest Distance to Target Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1182 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-distance-to-target-color](https://leetcode.com/problems/shortest-distance-to-target-color/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-distance-to-target-color/).

### Goal
Given an array of colors `1`, `2`, and `3`, answer queries asking for the shortest distance from an index to any occurrence of a target color.

### Function Contract
**Inputs**

- `colors`: List where each value is `1`, `2`, or `3`.
- `queries`: Each query is `[index, color]`.

**Return value**

List of shortest distances, using `-1` when the target color does not appear.

### Examples
**Example 1**

- Input: `colors = [1,1,2,1,3,2,2,3,3]`, `queries = [[1,3],[2,2],[6,1]]`
- Output: `[3,0,3]`

**Example 2**

- Input: `colors = [1,2]`, `queries = [[0,3]]`
- Output: `[-1]`

**Example 3**

- Input: `colors = [2,2,1]`, `queries = [[2,2],[0,1]]`
- Output: `[1,2]`

---

## Solution
### Approach
Store the sorted positions for each color. For a query `(index, color)`, binary search the target color's position list to find the insertion point for `index`.

Only the nearest position on the left and the nearest position on the right can be optimal, so compare those candidates.

### Complexity Analysis
- **Time Complexity**: `O(n + q log n)`, where `q` is the number of queries.
- **Space Complexity**: `O(n)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
