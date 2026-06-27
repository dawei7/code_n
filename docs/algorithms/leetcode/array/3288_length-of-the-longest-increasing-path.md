# Length of the Longest Increasing Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3288 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Sorting |
| Official Link | [length-of-the-longest-increasing-path](https://leetcode.com/problems/length-of-the-longest-increasing-path/) |

## Problem Description & Examples
### Goal
Given a 2D grid of points and a starting coordinate, determine the length of the longest sequence of points such that each subsequent point has both a strictly greater x-coordinate and a strictly greater y-coordinate than the previous point, starting from the given origin.

### Function Contract
**Inputs**

- `coordinates`: A list of lists of integers, where each inner list `[x, y]` represents a point in a 2D plane.
- `k`: A list of two integers `[kx, ky]` representing the starting point.

**Return value**

- An integer representing the maximum number of points in an increasing sequence that includes the starting point `k`.

### Examples
**Example 1**

- Input: `coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]]`, `k = [2,2]`
- Output: `3`
- Explanation: One possible path is `[0,0] -> [2,2] -> [5,3]`.

**Example 2**

- Input: `coordinates = [[2,1],[7,0],[5,6]]`, `k = [2,1]`
- Output: `2`
- Explanation: One possible path is `[2,1] -> [5,6]`.

**Example 3**

- Input: `coordinates = [[4,5],[2,2],[6,7],[2,3],[5,4],[3,3]]`, `k = [3,3]`
- Output: `4`
- Explanation: One possible path is `[2,2] -> [3,3] -> [5,4] -> [6,7]`.

---

## Underlying Base Algorithm(s)
The problem is a variation of the "Longest Increasing Subsequence" (LIS) problem. We split the points into two sets: those that can precede `k` (where `x < kx` and `y < ky`) and those that can follow `k` (where `x > kx` and `y > ky`). For the preceding set, we sort by `x` ascending and `y` ascending to find the LIS. For the following set, we sort by `x` ascending and `y` descending to find the LIS. The result is `1 + LIS(preceding) + LIS(following)`.

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of coordinates, due to sorting and the binary search approach for LIS.
- **Space Complexity**: `O(N)` to store the filtered points and the auxiliary array for the LIS calculation.
