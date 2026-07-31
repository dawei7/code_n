## Function Contract

**Inputs**

- `n`: The number of tasks in the project.
- `edges`: The `n - 1` undirected pairs `[u, v]` that form a valid tree over tasks `0` through `n - 1`.
- `baseTime`: A list where `baseTime[i]` is the positive base completion time of task `i`.

**Return value**

Return the minimum possible finish time of the chosen root after orienting the tree away from that root and applying the leaf and non-leaf finish-time rules recursively.
