# Count Unguarded Cells in the Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2257 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-unguarded-cells-in-the-grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/).

### Goal
Count empty grid cells seen by no guard. A guard watches horizontally and vertically until the grid edge or the first guard or wall blocks that direction.

### Function Contract
**Inputs**

- `m`, `n`: grid dimensions.
- `guards`: guard coordinates.
- `walls`: wall coordinates.

**Return value**

The number of cells containing neither guard nor wall that remain unguarded.

### Examples
**Example 1**

- Input: `m = 4`, `n = 6`, `guards = [[0, 0], [1, 1], [2, 3]]`, `walls = [[0, 1], [2, 2], [1, 4]]`
- Output: `7`

**Example 2**

- Input: `m = 3`, `n = 3`, `guards = [[1, 1]]`, `walls = []`
- Output: `4`

**Example 3**

- Input: `m = 1`, `n = 1`, `guards = []`, `walls = []`
- Output: `1`

---

## Solution
### Approach
Mark guards and walls in a grid. Sweep every row in both directions and every column in both directions, carrying whether an unobstructed guard has been encountered. Mark empty cells seen during any sweep, then count empty cells never marked.

### Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(mn)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
