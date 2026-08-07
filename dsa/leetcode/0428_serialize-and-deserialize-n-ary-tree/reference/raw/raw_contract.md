## Function Contract

**Inputs**

- `root`: An N-ary `Node` that begins the structure, or `None` for an empty tree. Each node exposes `val` and an ordered
  `children` list.

Canonical JSON fixtures encode an app-local node recursively as `[value, children]`; the runner constructs `Node`
objects before calling `solve`.

**Return value**

The app adapter serializes `root`, deserializes that string, and returns the reconstructed `Node`. The immutable
native artifact exposes the source-required `Codec.serialize(root)` and `Codec.deserialize(data)` methods.
