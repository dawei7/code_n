## Function Contract

**Inputs**

- `root`: An N-ary `Node` that begins the structure, or `None` for an empty tree. Each node exposes `val` and an
  ordered `children` list.

Canonical JSON fixtures encode an app-local node recursively as `[value, children]`; the runner constructs `Node`
objects before calling `solve`.

**Return value**

Return one list of node values per occupied depth, ordered from the root downward and from left to right within each
level.
