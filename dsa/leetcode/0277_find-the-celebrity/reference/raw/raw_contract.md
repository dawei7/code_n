## Function Contract

**Inputs**

- `n`: The number of people, labeled from `0` through `n - 1`.
- `knows_matrix`: The offline app's relationship matrix; its truthy entry at `[a][b]` represents `knows(a, b)`.

**Return value**

Return the celebrity's label, or `-1` if no celebrity exists. The native interface receives only `n` and queries the supplied `knows(a, b)` API.
