# Closest Room

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1847 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Sorting, Ordered Set |
| Official Link | [closest-room](https://leetcode.com/problems/closest-room/) |

## Problem Description & Examples
### Goal
For each query, choose a room whose size is at least the requested minimum and whose id is closest to the preferred id. Break ties by smaller id.

### Function Contract
**Inputs**

- `rooms`: a list of `[roomId, size]` pairs.
- `queries`: a list of `[preferredId, minSize]` pairs.

**Return value**

Return the chosen room id for each query, or `-1` if no room is large enough.

### Examples
**Example 1**

- Input: `rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]`
- Output: `[3,-1,3]`

**Example 2**

- Input: `rooms = [[1,4],[2,3],[3,5],[4,1]], queries = [[2,3],[2,4],[2,5]]`
- Output: `[2,1,3]`

**Example 3**

- Input: `rooms = [[10,2]], queries = [[5,1],[20,3]]`
- Output: `[10,-1]`

---

## Underlying Base Algorithm(s)
Process queries offline by decreasing `minSize`. Sort rooms by decreasing size and add all rooms large enough for the current query to an ordered set of room ids. Then binary search around the preferred id to test the nearest candidate on the left and right, choosing the smaller distance and then smaller id.

---

## Complexity Analysis
- **Time Complexity**: `O((n + q) log n)`
- **Space Complexity**: `O(n + q)`
