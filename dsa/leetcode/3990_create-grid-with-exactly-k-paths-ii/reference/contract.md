## Function Contract

`solve(k) -> list[str]`

**Inputs**

- `k`: The required positive number of valid right/down paths.

Rows and columns use zero-based indices. The dimensions $m$ and $n$ are selected by the returned construction rather than supplied as inputs.

**Output**

Return a non-empty list of at most 25 strings, each having the same positive length of at most 25. Every character must be `.` or `#`, both corner cells must be usable by the required paths, and the grid must contain exactly `k` paths from `(0, 0)` to `(m - 1, n - 1)` using only right and down moves. Different valid constructions are equivalent answers. Return `[]` only when no permitted grid exists.
