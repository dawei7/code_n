# Number of Valid Move Combinations On Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2056 |
| Difficulty | Hard |
| Topics | Array, String, Backtracking, Simulation |
| Official Link | [number-of-valid-move-combinations-on-chessboard](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/) |

## Problem Description & Examples
### Goal
Several chess pieces choose a destination and move one square per second along a legal direction, or stay still. Count destination choices where no two pieces ever occupy the same square at the same time.

### Function Contract
**Inputs**

- `pieces`: piece types `"rook"`, `"bishop"`, or `"queen"`.
- `positions`: starting squares using 1-based `[row, col]`.

**Return value**

Return the number of valid simultaneous move combinations.

### Examples
**Example 1**

- Input: `pieces = ["rook"], positions = [[1,1]]`
- Output: `15`

**Example 2**

- Input: `pieces = ["queen"], positions = [[1,1]]`
- Output: `22`

**Example 3**

- Input: `pieces = ["bishop"], positions = [[4,3]]`
- Output: `12`

---

## Underlying Base Algorithm(s)
Generate every legal movement option for each piece, including staying. Backtrack over option choices and simulate each second up to the maximum movement length; reject a combination if two pieces share a square at any time.

---

## Complexity Analysis
- **Time Complexity**: exponential in the number of pieces, bounded by the small board and piece count constraints.
- **Space Complexity**: `O(p)` plus generated move options.
