## Function Contract

**Inputs**

- `n`: The number of tasks in the rooted tree.
- `edges`: The `n - 1` directed parent-child pairs `[u, v]` that describe the tree rooted at `0`.
- `baseTime`: A list where `baseTime[i]` is the positive base duration of task `i`.

**Return value**

Return the finish time of task `0` after applying the leaf and non-leaf rules recursively throughout the tree. The result is guaranteed to be exactly representable as an integer below $2^{53}$.
