# Queens That Can Attack the King

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1222 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [queens-that-can-attack-the-king](https://leetcode.com/problems/queens-that-can-attack-the-king/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/queens-that-can-attack-the-king/).

### Goal
On an `8 x 8` chessboard, return every queen that can attack the king along a row, column, or diagonal without another queen blocking the path.

### Function Contract
**Inputs**

- `queens`: coordinates of queens.
- `king`: coordinate of the king.

**Return value**

Coordinates of attacking queens. Order is not important.

### Examples
**Example 1**

- Input: `queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]`, `king = [0,0]`
- Output: `[[0,1],[1,0],[3,3]]`

**Example 2**

- Input: `queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]`, `king = [3,3]`
- Output: `[[2,2],[3,4],[4,4]]`

**Example 3**

- Input: `queens = [[5,6],[7,7],[2,1]]`, `king = [4,5]`
- Output: `[[5,6]]`

---

## Solution
### Approach
Directional ray scanning on a grid.

### Complexity Analysis
- **Time Complexity**: `O(q + 8 * board_size)`, effectively constant for an `8 x 8` board.
- **Space Complexity**: `O(q)` for the queen lookup set.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(queens, king):
    occupied = {tuple(queen) for queen in queens}
    answer = []
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        r, c = king[0] + dr, king[1] + dc
        while 0 <= r < 8 and 0 <= c < 8:
            if (r, c) in occupied:
                answer.append([r, c])
                break
            r += dr
            c += dc
    return answer
```
</details>
