# Find the Number of Ways to Place People I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3025 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Official Link | [find-the-number-of-ways-to-place-people-i](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/) |

## Problem Description & Examples
### Goal
Given a set of 2D points representing people on a grid, determine the number of pairs of points (A, B) such that A can "fence" B. A point A can fence point B if A is located at the top-left of B (i.e., $x_A \le x_B$ and $y_A \ge y_B$) and there are no other points located within the rectangular region defined by A and B, excluding A and B themselves.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list contains two integers `[x, y]` representing the coordinates of a person.

**Return value**

- An integer representing the total count of valid pairs (A, B) that satisfy the fencing condition.

### Examples
**Example 1**

- Input: `points = [[1,1],[2,2],[3,3]]`
- Output: `0`

**Example 2**

- Input: `points = [[6,2],[4,4]]`
- Output: `1`

**Example 3**

- Input: `points = [[3,1],[1,3],[1,1]]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem is solved using a sorting-based enumeration approach. First, we sort the points primarily by their x-coordinate (ascending) and secondarily by their y-coordinate (descending). This ordering ensures that for any pair (A, B) where A comes before B in the sorted list, A is guaranteed to be to the left of or at the same x-position as B. By iterating through all pairs and checking the y-coordinate condition ($y_A \ge y_B$) and verifying that no intermediate points exist within the rectangle, we can count the valid pairs.

---

## Complexity Analysis
- **Time Complexity**: $O(n^3)$, where $n$ is the number of points. We iterate through all pairs ($O(n^2)$) and for each pair, we iterate through all other points to check if they lie within the rectangle ($O(n)$).
- **Space Complexity**: $O(1)$ (excluding the space required for sorting), as we only use a few variables for counting and indexing.
