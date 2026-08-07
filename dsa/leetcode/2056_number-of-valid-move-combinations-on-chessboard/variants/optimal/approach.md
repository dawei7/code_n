## General
Given There is an `8 x 8` chessboard containing `n` pieces (rooks, queens, or bishops). You are given a string array `pieces` of length `n`, where $\text{pieces}[i]$ describes the type (rook, queen, or bishop) of the $$i^{\..., the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends.

## Complexity detail
- **Time Complexity**: $O(1)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
