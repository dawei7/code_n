# Find Winner on a Tic Tac Toe Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1275 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-winner-on-a-tic-tac-toe-game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/).

### Goal
Given the sequence of moves in a `3 x 3` tic-tac-toe game, report whether player A wins, player B wins, the game is a draw, or the game is still pending.

### Function Contract
**Inputs**

- `moves`: positions played in order; A moves first and players alternate.

**Return value**

`"A"`, `"B"`, `"Draw"`, or `"Pending"`.

### Examples
**Example 1**

- Input: `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`
- Output: `"A"`

**Example 2**

- Input: `moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]`
- Output: `"B"`

**Example 3**

- Input: `moves = [[0,0],[1,1]]`
- Output: `"Pending"`

---

## Solution
### Approach
Small-board simulation and line checking.

### Complexity Analysis
- **Time Complexity**: `O(1)` because the board size is fixed.
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(moves):
    board = [[0] * 3 for _ in range(3)]
    for turn, (r, c) in enumerate(moves):
        board[r][c] = 1 if turn % 2 == 0 else -1
    lines = board + [[board[r][c] for r in range(3)] for c in range(3)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    if any(sum(line) == 3 for line in lines):
        return "A"
    if any(sum(line) == -3 for line in lines):
        return "B"
    return "Draw" if len(moves) == 9 else "Pending"
```
</details>
