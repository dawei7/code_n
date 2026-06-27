# Minimize Manhattan Distances

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3102 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Sorting, Ordered Set |
| Official Link | [minimize-manhattan-distances](https://leetcode.com/problems/minimize-manhattan-distances/) |

## Problem Description & Examples
### Goal
Given a set of 2D points, determine the minimum possible maximum Manhattan distance between any two points in the set after removing exactly one point from the collection.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list contains two integers `[x, y]` representing the coordinates of a point.

**Return value**

- An integer representing the minimum possible value of the maximum Manhattan distance between any two remaining points after one point is removed.

### Examples
**Example 1**

- Input: `points = [[3,10],[5,15],[10,2],[4,4]]`
- Output: `12`

**Example 2**

- Input: `points = [[1,1],[1,1],[1,1]]`
- Output: `0`

**Example 3**

- Input: `points = [[3,10],[5,15],[10,2],[4,4],[1,1]]`
- Output: `14`

---

## Underlying Base Algorithm(s)
The Manhattan distance between $(x_1, y_1)$ and $(x_2, y_2)$ is $|x_1 - x_2| + |y_1 - y_2|$. This can be transformed using the coordinate rotation identity: $|x_1 - x_2| + |y_1 - y_2| = \max(|(x_1+y_1) - (x_2+y_2)|, |(x_1-y_1) - (x_2-y_2)|)$. By defining $u = x+y$ and $v = x-y$, the Manhattan distance becomes $\max(|u_1 - u_2|, |v_1 - v_2|)$. The maximum distance in the set is determined by the extreme values of $u$ and $v$. Removing a point that contributes to these extreme values is the only way to potentially reduce the maximum distance.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$ due to sorting the transformed coordinates (or $O(N)$ if using a single pass to find the top two extremes).
- **Space Complexity**: $O(N)$ to store the transformed coordinates.
