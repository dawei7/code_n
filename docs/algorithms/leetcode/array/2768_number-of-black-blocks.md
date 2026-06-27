# Number of Black Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2768 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Enumeration |
| Official Link | [number-of-black-blocks](https://leetcode.com/problems/number-of-black-blocks/) |

## Problem Description & Examples
### Goal
Given a grid of size `m x n` and a list of coordinates representing "black" cells, identify how many 2x2 subgrids contain exactly 0, 1, 2, 3, or 4 black cells. A 2x2 subgrid is defined by its top-left corner `(r, c)`, where `0 <= r < m-1` and `0 <= c < n-1`.

### Function Contract
**Inputs**

- `m`: An integer representing the number of rows.
- `n`: An integer representing the number of columns.
- `coordinates`: A list of lists, where each inner list `[r, c]` denotes the position of a black cell.

**Return value**

- A list of 5 integers where the index `i` represents the number of 2x2 subgrids containing exactly `i` black cells.

### Examples
**Example 1**

- Input: `m = 3, n = 3, coordinates = [[0,0]]`
- Output: `[3, 1, 0, 0, 0]`

**Example 2**

- Input: `m = 3, n = 3, coordinates = [[0,0],[1,1],[0,2]]`
- Output: `[0, 2, 2, 0, 0]`

---

## Underlying Base Algorithm(s)
The problem is solved using a Hash Map (dictionary) to track the count of black cells for every affected 2x2 subgrid. Since a single black cell at `(r, c)` can be part of at most four 2x2 subgrids (top-left corners: `(r-1, c-1), (r-1, c), (r, c-1), (r, c)`), we iterate through the given coordinates, calculate these potential top-left corners, and increment their counts in the map if they fall within the valid grid boundaries. Finally, we calculate the number of subgrids with 0 black cells by subtracting the number of subgrids that have at least one black cell from the total possible 2x2 subgrids `(m-1) * (n-1)`.

## Complexity Analysis
- **Time Complexity**: `O(K)`, where `K` is the number of black cells. We perform a constant number of operations (at most 4) for each coordinate.
- **Space Complexity**: `O(K)`, as we store the counts of affected 2x2 subgrids in a hash map, which can contain at most `4K` entries.
