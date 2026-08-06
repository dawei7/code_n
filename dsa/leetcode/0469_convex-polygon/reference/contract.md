## Function Contract

**Inputs**

- `points`: The unique polygon vertices `[x_i, y_i]` in sequential boundary order.

**Return value**

- Return `True` if the polygon is convex; otherwise, return `False`.

The given order already defines the polygon boundary, including the closing edge from the final point back to the first.
