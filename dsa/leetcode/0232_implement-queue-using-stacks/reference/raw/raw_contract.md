## Function Contract

**Inputs**

- `operations`: App-local method names selected from `push`, `pop`, `peek`, and `empty`.
- `values`: The corresponding integer for each `push`, or `null` for a method with no argument.

**Return value**

Return an aligned result for every operation: `null` for `push`, the affected value for `peek` or `pop`, and a boolean for `empty`.
