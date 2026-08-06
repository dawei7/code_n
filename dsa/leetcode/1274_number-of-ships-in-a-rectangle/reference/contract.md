## Function Contract

**Inputs**

- `sea`: a hidden `Sea` object whose only problem-authorized observation is `hasShips(topRight, bottomLeft)`.
- `topRight`: a `Point` with fields `x` and `y` giving the upper-right corner $(x_2, y_2)$ of the target rectangle.
- `bottomLeft`: a `Point` with fields `x` and `y` giving the lower-left corner $(x_1, y_1)$ of the target rectangle.

For an ordered query rectangle, `sea.hasShips(topRight, bottomLeft)` returns `true` exactly when at least one hidden ship lies inside it, including on its boundary. The `ships` data shown in examples initializes the judge's hidden map; it is not supplied as an accessible parameter to the solution.

Let $s$ be the number of ships in the target rectangle, and let

$$
C = \max(x_2 - x_1 + 1,\ y_2 - y_1 + 1)
$$

be the larger inclusive side length.

**Return value**

- Return the number $s$ of hidden ship points in the inclusive target rectangle while using at most $400$ calls to `hasShips`.
