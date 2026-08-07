## Function Contract

**Inputs**

- `root`: An N-ary `Node` that begins the structure, or `None` for an empty tree. Each node exposes `val` and an
  ordered `children` list.

Canonical JSON fixtures encode an app-local node recursively as `[value, children]`; the runner constructs `Node`
objects before calling `solve`.

**Return value**

The app adapter encodes `root` as a binary `TreeNode`, decodes that representation, and returns the reconstructed
N-ary `Node`. The immutable native artifact exposes the source-required `Codec.encode(root)` and
`Codec.decode(data)` methods.
