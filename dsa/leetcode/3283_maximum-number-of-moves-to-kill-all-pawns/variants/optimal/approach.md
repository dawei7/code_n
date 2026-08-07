## General
Given There is a `50 x 50` chessboard with **one** knight and some pawns on it. You are given two integers `kx` and `ky` where `(kx, ky)` denotes the position of the knight, and a 2D array `positions` where $\text{positions..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

## Complexity detail
- **Time Complexity**: $O(p B + p^2 2^p)$ — Operation count bound.
- **Space Complexity**: $O(B + p 2^p)$ — Auxiliary memory allocation bound.
