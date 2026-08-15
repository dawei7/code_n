# Count Artifacts That Can Be Extracted

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/) |

## Problem Description

### Goal

An $n \times n$ 0-indexed grid contains non-overlapping rectangular artifacts. Each artifact description `[r1, c1, r2, c2]` gives its inclusive top-left and bottom-right cells. Every artifact occupies at most four cells.

The coordinates in `dig` are the distinct cells whose mud will be removed. Digging a cell uncovers any artifact part there, and an artifact can be extracted only when every cell in its rectangle has been dug. Return the number of completely uncovered artifacts.

### Function Contract

**Inputs**

- `n`: the grid side length, where $1 \le n \le 1000$.
- `artifacts`: between $1$ and $\min(n^2,10^5)$ non-overlapping inclusive rectangles, each covering at most four cells.
- `dig`: between $1$ and $\min(n^2,10^5)$ unique in-bounds cell coordinates.

Let $a$ be the number of artifacts and $d$ the number of dug cells.

**Return value**

Return the number of artifacts for which every covered grid cell appears in `dig`.

### Examples

#### Example 1

- **Input:** `n = 2`, `artifacts = [[0,0,0,0],[0,1,1,1]]`, `dig = [[0,0],[0,1]]`
- **Output:** `1`

The single-cell artifact is complete, but the vertical artifact still has an undug cell at `(1,1)`.

#### Example 2

- **Input:** `n = 2`, `artifacts = [[0,0,0,0],[0,1,1,1]]`, `dig = [[0,0],[0,1],[1,1]]`
- **Output:** `2`

Every cell belonging to either artifact has been dug.
