## Function Contract

**Inputs**

- `start`: Two zero-based coordinates `[x, y]` for the starting cell.
- `target`: Two zero-based coordinates `[x, y]` for the destination cell.

Both coordinates of both cells are between `0` and `7`, inclusive.

**Return value**

Return `true` when at least one legal knight route from `start` to `target` contains an even number of moves, including the zero-move route when the cells are equal. Return `false` otherwise.
