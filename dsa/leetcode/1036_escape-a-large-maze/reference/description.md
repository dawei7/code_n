## Description

There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are `(x, y)`.

We start at the `source = [s_x, s_y]` square and want to reach the `target = [t_x, t_y]` square. There is also an array of `blocked` squares, where each `blocked[i] = [x_i, y_i]` represents a blocked square with coordinates `(x_i, y_i)`.

Each move, we can walk one square north, east, south, or west if the square is **not** in the array of `blocked` squares. We are also not allowed to walk outside of the grid.

Return `true`* if and only if it is possible to reach the *`target`* square from the *`source`* square through a sequence of valid moves*.
