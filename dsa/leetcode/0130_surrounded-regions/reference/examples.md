## Examples

**Example 1**

- Input: `board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]`
- Output: `[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]`
- Explanation: The three interior `'O'` cells form a surrounded region and are captured. The bottom `'O'` remains because it lies on the board's edge and therefore cannot be surrounded.

```text
Before       After
X X X X      X X X X
X O O X  ->  X X X X
X X O X      X X X X
X O X X      X O X X
  ^              ^
edge cell remains unchanged
```

**Example 2**

- Input: `board = [["X"]]`
- Output: `[["X"]]`
