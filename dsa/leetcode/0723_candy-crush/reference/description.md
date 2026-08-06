## Description

This task implements the elimination process used by Candy Crush. You are given an $m \times n$ integer matrix `board` describing the game immediately after a player's move. Each positive value identifies a candy type, while `0` represents an empty cell created during the simulation.

Restore the game to a stable state by applying these rules in order:

1. Whenever three or more equal candies are adjacent horizontally or vertically, crush every candy in every qualifying run simultaneously. Those cells become empty.
2. After that simultaneous crush, candies above empty cells fall together until each reaches another candy or the bottom. No new candy enters through the top boundary.
3. If gravity creates another qualifying run, repeat the crush and gravity steps.
4. When no candy can be crushed, the board is stable; return that current board.

Continue applying complete rounds until the returned board is stable.
