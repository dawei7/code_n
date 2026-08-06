## Function Contract

**Inputs**

- `robot`: an opaque robot interface positioned on an empty room cell

The interface provides four operations:

- `robot.move()` attempts one forward step. It returns `True` after entering an open cell, or `False` when an
  obstacle blocks the step and the robot remains in place.
- `robot.turnLeft()` rotates the robot $90$ degrees left without changing its cell.
- `robot.turnRight()` rotates the robot $90$ degrees right without changing its cell.
- `robot.clean()` cleans the current cell.

**Return value**

- Return `None`; success is the side effect of cleaning every empty cell reachable from the starting position.

The solution must operate only through this interface and must not inspect the hidden grid.
