# Cherry Pickup II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1463 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [cherry-pickup-ii](https://leetcode.com/problems/cherry-pickup-ii/) |

## Problem Description & Examples
### Goal
Two robots start at the top row, one at the leftmost column and one at the rightmost column. On each step both move to the next row and may shift left, stay, or shift right. Maximize the total cherries collected.

### Function Contract
**Inputs**

- `grid`: a matrix where each cell contains cherries.

**Return value**

The maximum number of cherries both robots can collect.

### Examples
**Example 1**

- Input: `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]`
- Output: `24`

**Example 2**

- Input: `grid = [[1,0,0,0],[0,0,0,0],[0,0,2,0]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,1],[1,1]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Row-by-row dynamic programming over the two robot columns. Each state `(row, c1, c2)` stores the best cherries after both robots reach those columns; transitions try all nine next-column pairs.

---

## Complexity Analysis
- **Time Complexity**: `O(rows * cols^2 * 9)`
- **Space Complexity**: `O(cols^2)` with rolling rows.
