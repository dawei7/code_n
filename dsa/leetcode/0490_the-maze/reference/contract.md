## Function Contract

**Inputs**

- `maze`: a rectangular matrix where `0` is an empty space and `1` is a wall
- `start`: the ball's initial empty cell as `[row, column]`
- `destination`: the distinct empty cell where the ball must stop

**Return value**

- Return `True` if some sequence of complete rolls stops at `destination`; otherwise return `False`.

Each chosen direction is committed until a wall stops the ball. Intermediate cells crossed during that roll are not
decision points.
