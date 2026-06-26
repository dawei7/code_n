# Cat and Mouse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1728 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Matrix, Game Theory |
| Official Link | [cat-and-mouse-ii](https://leetcode.com/problems/cat-and-mouse-ii/) |

## Problem Description & Examples
### Goal
A mouse and a cat move on a grid with walls, food, and jump limits. The mouse moves first. The mouse wins by reaching food; the cat wins by catching the mouse, reaching food first, or forcing the game beyond the move limit. Determine whether the mouse can force a win.

### Function Contract
**Inputs**

- `grid`: a list of strings describing open cells, walls, mouse, cat, and food.
- `catJump`: the cat's maximum jump distance per turn.
- `mouseJump`: the mouse's maximum jump distance per turn.

**Return value**

Return `True` if the mouse has a forced win, otherwise `False`.

### Examples
**Example 1**

- Input: `grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2`
- Output: `True`

**Example 2**

- Input: `grid = ["M.C...F"], catJump = 1, mouseJump = 4`
- Output: `True`

**Example 3**

- Input: `grid = ["M.C...F"], catJump = 1, mouseJump = 3`
- Output: `False`

---

## Underlying Base Algorithm(s)
Model the game as states `(mouse_position, cat_position, turn, moves)` and solve by memoized minimax. Generate all legal moves up to the current player's jump distance, including staying put. Terminal states cover mouse at food, cat at food, cat meeting mouse, and the move-limit draw that favors the cat. The current player chooses any move leading to their win; otherwise the state is losing.

---

## Complexity Analysis
- **Time Complexity**: `O(R^2 * C^2 * L * (R + C))`, where `L` is the move limit
- **Space Complexity**: `O(R^2 * C^2 * L)`
