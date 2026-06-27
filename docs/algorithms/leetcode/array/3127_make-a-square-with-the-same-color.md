# Make a Square with the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3127 |
| Difficulty | Easy |
| Topics | Array, Matrix, Enumeration |
| Official Link | [make-a-square-with-the-same-color](https://leetcode.com/problems/make-a-square-with-the-same-color/) |

## Problem Description & Examples
### Goal
Given a 3x3 grid containing characters 'B' (black) and 'W' (white), determine if it is possible to form a 2x2 square consisting of cells of the same color by changing at most one cell's color.

### Function Contract
**Inputs**

- `grid`: A list of lists of characters (3x3 matrix) where each element is either 'B' or 'W'.

**Return value**

- `bool`: Returns `True` if a monochromatic 2x2 square can be formed, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = [["B","W","B"],["B","W","W"],["B","W","B"]]`
- Output: `True`

**Example 2**

- Input: `grid = [["B","W","B"],["W","B","W"],["B","W","B"]]`
- Output: `False`

**Example 3**

- Input: `grid = [["B","W","B"],["B","W","W"],["W","W","B"]]`
- Output: `True`

---

## Underlying Base Algorithm(s)
The problem is solved using **Brute Force Enumeration**. Since the grid is fixed at 3x3, there are exactly four possible 2x2 sub-grids. For each sub-grid, we count the occurrences of 'B' and 'W'. If either color appears 3 or 4 times, it implies that with at most one change, we can make all four cells the same color.

---

## Complexity Analysis
- **Time Complexity**: O(1). The grid size is constant (3x3), and we perform a fixed number of operations (checking 4 sub-grids).
- **Space Complexity**: O(1). We only use a constant amount of extra space for counters.
