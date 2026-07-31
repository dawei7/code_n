# Count Covered Buildings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3531 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-covered-buildings/) |

## Problem Description

### Goal

An $n \times n$ city uses coordinates from $1$ through $n$ on both axes. Each unique pair `[x, y]` in `buildings` identifies one occupied coordinate.

A building at `[x, y]` is covered only when four other buildings exist in its cardinal directions: one above it and one below it in the same column, plus one to its left and one to its right in the same row. They need not be adjacent; any strictly smaller or larger coordinate in the required row or column qualifies. Diagonal buildings do not satisfy a direction.

Return the number of covered buildings.

### Function Contract

**Inputs**

- `n`: The side length of the city, where $2 \le n \le 10^5$.
- `buildings`: A list of distinct coordinates `[x, y]`, with $1 \le x,y \le n$.

Let $B = \lvert\texttt{buildings}\rvert$, where $1 \le B \le 10^5$.

**Return value**

- The number of coordinates that have another building strictly above, below, left, and right in the same column or row.

### Examples

**Example 1**

- Input: `n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]`
- Output: `1`
- Explanation: `[2,2]` has a building in every cardinal direction; each arm of the cross is missing at least one direction.

**Example 2**

- Input: `n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]`
- Output: `0`
- Explanation: Every building lies on the boundary of the occupied square and lacks at least one required direction.

**Example 3**

- Input: `n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]`
- Output: `1`
- Explanation: `[3,3]` is covered even though the buildings above, below, and to the right are not adjacent to it.
