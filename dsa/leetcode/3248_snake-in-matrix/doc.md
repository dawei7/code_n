# Snake in Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3248 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [snake-in-matrix](https://leetcode.com/problems/snake-in-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/snake-in-matrix/).

### Goal
Given an $n \times n$ grid where cells are numbered from $0$ to $n^2 - 1$ in row-major order, simulate the movement of a snake starting at position $0$. You are provided with a sequence of directional commands ("UP", "DOWN", "LEFT", "RIGHT"). The goal is to determine the final cell number occupied by the snake after executing all commands.

### Function Contract
**Inputs**

- `n`: An integer representing the dimensions of the $n \times n$ grid.
- `commands`: A list of strings representing the sequence of moves.

**Return value**

- An integer representing the final cell index after all moves are processed.

### Examples
**Example 1**

- Input: `n = 2, commands = ["RIGHT", "DOWN"]`
- Output: `3`

**Example 2**

- Input: `n = 3, commands = ["DOWN", "RIGHT", "UP"]`
- Output: `1`

**Example 3**

- Input: `n = 2, commands = ["UP", "DOWN"]`
- Output: `0`

---

## Solution
### Approach
The problem is a direct simulation. Since the grid is indexed row-major, a cell at `(row, col)` corresponds to the value `row * n + col`. We maintain the current `(r, c)` coordinates, update them based on the command, and calculate the final index using the formula `r * n + c`.

### Complexity Analysis
- **Time Complexity**: $O(k)$, where $k$ is the number of commands, as we process each command exactly once.
- **Space Complexity**: $O(1)$, as we only store the current row and column indices regardless of the grid size.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, commands: list[str]) -> int:
    """
    Simulates the snake movement on an n x n grid.
    The grid cells are numbered 0 to n^2 - 1.
    Position (r, c) maps to index r * n + c.
    """
    r, c = 0, 0

    for command in commands:
        if command == "UP":
            r -= 1
        elif command == "DOWN":
            r += 1
        elif command == "LEFT":
            c -= 1
        elif command == "RIGHT":
            c += 1

    return r * n + c
```
</details>
