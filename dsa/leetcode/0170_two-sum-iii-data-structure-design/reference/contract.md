## Function Contract

The app executes the stateful class through an equivalent operation-list adapter.

**Inputs**

- `operations`: The constructor, `add`, and `find` operations in execution order.
- `arguments`: The argument list corresponding to each operation.

**Return value**

Return one aligned result per operation: `null` for construction and additions, and the boolean result for each `find`.
