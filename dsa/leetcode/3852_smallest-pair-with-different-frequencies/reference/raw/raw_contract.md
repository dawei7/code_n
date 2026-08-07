## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

For every value $v$ that occurs in `nums`, let $f(v)$ denote its frequency. A candidate pair must consist of two distinct present values and satisfy

$$
x < y \quad\text{and}\quad f(x) \ne f(y).
$$

Pairs are ordered lexicographically: a smaller `x` takes priority, and `y` breaks ties only when `x` is equal.

**Return value**

Return `[x, y]` for the lexicographically smallest valid pair. Return `[-1, -1]` when no valid pair exists.
