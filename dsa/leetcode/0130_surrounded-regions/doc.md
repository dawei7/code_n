# Surrounded Regions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 130 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/surrounded-regions/) |

## Problem Description
### Goal
Given a rectangular board containing only `"X"` and `"O"`, identify regions of `"O"` cells connected through shared horizontal or vertical sides. A region is surrounded when none of its cells lies on the board boundary and no cell in the region can reach a boundary `"O"` through such connections.

Capture every surrounded region by changing all of its cells to `"X"` in place. Any boundary `"O"`, along with every `"O"` connected to it, must remain unchanged because that region is open to the outside. Diagonal contact does not connect regions, and the function returns no separate replacement board.

### Function Contract
**Inputs**

- `board`: a rectangular matrix containing only `"X"` and `"O"`

**Return value**

`None`; mutate `board` in place to capture all surrounded regions.

### Examples
**Example 1**

- Input: `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`
- Output board: `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

**Example 2**

- Input: `board = [["X"]]`
- Output board: `[["X"]]`

**Example 3**

- Input: `board = [["O","O"],["X","O"]]`
- Output board unchanged
