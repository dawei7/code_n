# Minimum Knight Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1197 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-knight-moves](https://leetcode.com/problems/minimum-knight-moves/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-knight-moves/).

### Goal
On an infinite chessboard, return the minimum number of knight moves needed to travel from `(0, 0)` to `(x, y)`.

### Function Contract
**Inputs**

- `x`: Target x-coordinate.
- `y`: Target y-coordinate.

**Return value**

Minimum number of knight moves.

### Examples
**Example 1**

- Input: `x = 2`, `y = 1`
- Output: `1`

**Example 2**

- Input: `x = 5`, `y = 5`
- Output: `4`

**Example 3**

- Input: `x = 0`, `y = 0`
- Output: `0`

---

## Solution
### Approach
Use board symmetry and work with `abs(x)` and `abs(y)`. A breadth-first search from `(0, 0)` over knight moves finds the shortest distance. The search only needs a bounded region around the first quadrant, with a small negative margin to handle short paths that step backward.

There are also mathematical solutions, but bounded BFS is straightforward and reliable for the problem limits.

### Complexity Analysis
- **Time Complexity**: `O((|x| + |y|)^2)` for bounded BFS.
- **Space Complexity**: `O((|x| + |y|)^2)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
