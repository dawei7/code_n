## Description

You stand at the unique `S` cell of a rectangular grid and want to reach the unique destination `D`. Empty cells are `.`, stones are `X`, and initially flooded cells are `*`. Each second you may move one cell orthogonally, while flooding simultaneously spreads from every flooded cell into adjacent empty cells.

You may never enter a stone or flooded cell. A move is also invalid when its destination becomes flooded during that same second. The destination never floods. Return the fewest seconds needed to reach `D`, or `-1` when every possible journey is blocked or overtaken by water.
