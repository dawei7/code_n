# Number of Valid Move Combinations On Chessboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2056 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Backtracking, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/) |

## Problem Description

### Goal

An $8\times8$ chessboard contains up to four distinct pieces, each a rook, bishop, or queen. For every piece, choose a destination reachable in one legal straight direction; choosing its current square is also allowed. All chosen moves begin together at second zero.

At each following second, a piece that has not reached its destination advances exactly one square along its chosen direction, while a finished piece remains still. A move combination is valid only if no two pieces occupy the same square at any integer time. Pieces may swap adjacent squares during one second because they never share a square at either endpoint. Count all valid combinations of destinations.

### Function Contract

**Inputs**

- `pieces`: an array of $p$ values from `"rook"`, `"bishop"`, and `"queen"`, where $1 \le p \le 4$ and at most one value is `"queen"`.
- `positions`: distinct one-based squares `[row, column]`, with both coordinates from $1$ through $8$, corresponding to `pieces`.

**Return value**

- Return the number of simultaneous destination choices that never place two pieces on one square at the same integer second.

### Examples

**Example 1**

- Input: `pieces = ["rook"], positions = [[1,1]]`
- Output: `15`
- Explanation: The rook may stay or choose any of the other fourteen squares in its row or column.

**Example 2**

- Input: `pieces = ["queen"], positions = [[1,1]]`
- Output: `22`

**Example 3**

- Input: `pieces = ["bishop"], positions = [[4,3]]`
- Output: `12`
