# Move Pieces to Obtain a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2337 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) |

## Problem Description

### Goal

Two strings describe rows of pieces and empty cells. Each string has the same
length and contains only `L`, `R`, and `_`. An `L` piece may move into an
adjacent empty cell on its left, while an `R` piece may move into an adjacent
empty cell on its right. Pieces cannot move in the opposite direction or pass
through one another.

Determine whether a sequence of any number of legal moves can transform
`start` into `target`. The arrangement must therefore preserve the left-to-right
order and type of every piece, while each piece must also be able to reach its
target position using only its permitted direction.

### Function Contract

**Inputs**

- `start`: A string of length $n$ describing the initial arrangement.
- `target`: A string of the same length describing the desired arrangement.

Both strings contain only `L`, `R`, and `_`, with $1 \le n \le 10^5$.

**Return value**

`True` if legal moves can transform `start` into `target`; otherwise `False`.

### Examples

#### Example 1

- **Input:** `start = "_L__R__R_"`, `target = "L______RR"`
- **Output:** `True`
- **Explanation:** The `L` can move left once, and the two `R` pieces can move
  right to their target cells without crossing another piece.

#### Example 2

- **Input:** `start = "R_L_"`, `target = "__LR"`
- **Output:** `False`
- **Explanation:** The `R` would have to pass the `L`, which no legal move allows.

#### Example 3

- **Input:** `start = "_R"`, `target = "R_"`
- **Output:** `False`
- **Explanation:** An `R` piece cannot move left.
