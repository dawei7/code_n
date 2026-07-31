## Function Contract

**Inputs**

- `operations`: A sequence of method names beginning with `LRUCache`, followed by `get` and `put` calls.
- `arguments`: One argument list per operation. The constructor receives the capacity, `get` receives a key, and `put` receives a key and a value.

**Return value**

Return one result per operation: `null` for construction and `put`, and the stored value or `-1` for each `get`.
