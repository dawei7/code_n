# Paint House III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1473 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [paint-house-iii](https://leetcode.com/problems/paint-house-iii/) |

## Problem Description & Examples
### Goal
Paint unpainted houses so exactly `target` neighborhoods are formed, minimizing total paint cost. Already painted houses cannot change color.

### Function Contract
**Inputs**

- `houses`: color `0` means unpainted; positive values are fixed colors.
- `cost`: `cost[i][c]` is the cost to paint house `i` with color `c + 1`.
- `m`: number of houses.
- `n`: number of colors.
- `target`: required number of neighborhoods.

**Return value**

The minimum total cost, or `-1` if the target neighborhood count is impossible.

### Examples
**Example 1**

- Input: `houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `9`

**Example 2**

- Input: `houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3`
- Output: `11`

**Example 3**

- Input: `houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Dynamic programming by house index, last color, and neighborhood count. For each house, try the allowed colors and add a neighborhood when the color differs from the previous house.

---

## Complexity Analysis
- **Time Complexity**: `O(m * target * n^2)`
- **Space Complexity**: `O(target * n)` with rolling rows.
