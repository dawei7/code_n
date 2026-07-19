# Prison Cells After N Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 957 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [prison-cells-after-n-days](https://leetcode.com/problems/prison-cells-after-n-days/) |

## Problem Description

### Goal

Eight prison cells form a row. Each cell is occupied (`1`) or vacant (`0`). Every day all cells update simultaneously from the previous day's state: an interior cell becomes occupied when its two adjacent neighbors are equal, whether both occupied or both vacant, and becomes vacant otherwise.

The first and last cells lack two neighbors, so they become vacant after every update. Given the initial `cells` state and a positive day count `n`, return the complete eight-cell state after exactly `n` daily updates.

### Function Contract

**Inputs**

- `cells`: a list of exactly eight values, each either `0` or `1`.
- `n`: the number of simultaneous daily updates, where $1 \le n \le 10^9$.

**Return value**

Return the eight occupancy values after exactly `n` days.

### Examples

**Example 1**

- Input: `cells = [0,1,0,1,1,0,0,1]`, `n = 7`
- Output: `[0,0,1,1,0,0,0,0]`

**Example 2**

- Input: `cells = [1,0,0,1,0,0,1,0]`, `n = 1000000000`
- Output: `[0,0,1,1,1,1,1,0]`
