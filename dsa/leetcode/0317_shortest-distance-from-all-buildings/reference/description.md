## Description

You are given an $m \times n$ grid `grid` whose cells contain `0`, `1`, or `2`:

- `0` denotes empty land through which travel is allowed.
- `1` denotes a building, which cannot be crossed.
- `2` denotes an obstacle, which also cannot be crossed.

Choose an empty cell on which to build a house so that every building is reachable and the sum of all building-to-house travel distances is as small as possible. Movement is limited to one cell up, down, left, or right.

Return that minimum total distance. If no empty cell can reach every building under these rules, return `-1`. The total distance is the sum of the individual shortest travel distances from all buildings to the chosen location.
