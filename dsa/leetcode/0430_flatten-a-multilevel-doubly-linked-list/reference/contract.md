## Function Contract

**Inputs**

- `head`: The first `Node` of the top-level doubly linked list, or `None`. Each node exposes `val`, `prev`, `next`,
  and `child`.

Canonical JSON fixtures encode each level as `[value, child_nodes]` entries; the runner reconstructs the full node
graph before calling `solve(head)`.

**Return value**

Return the first flattened `Node`. All `child` links must be `None`, and adjacent `next` and `prev` links must be
reciprocal.
