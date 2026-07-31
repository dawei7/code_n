## Description

You are given two integer arrays, `start` and `target`. Each has the form `[x, y]` and identifies one cell of a standard $8\times8$ chessboard.

A knight move changes one coordinate by two squares and the perpendicular coordinate by one square. From an interior cell `(x, y)`, the eight possible relative destinations are:

| Horizontal change | Vertical change | Destination |
|---:|---:|---|
| $+1$ | $+2$ | $(x+1,y+2)$ |
| $+2$ | $+1$ | $(x+2,y+1)$ |
| $-1$ | $+2$ | $(x-1,y+2)$ |
| $-2$ | $+1$ | $(x-2,y+1)$ |
| $+1$ | $-2$ | $(x+1,y-2)$ |
| $+2$ | $-1$ | $(x+2,y-1)$ |
| $-1$ | $-2$ | $(x-1,y-2)$ |
| $-2$ | $-1$ | $(x-2,y-1)$ |

Only destinations that remain on the board are legal. Return `true` if the knight can travel from `start` to `target` using an even number of moves; otherwise, return `false`.
