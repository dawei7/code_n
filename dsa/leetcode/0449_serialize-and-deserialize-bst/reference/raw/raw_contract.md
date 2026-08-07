## Function Contract

**Inputs**

- `root`: The root of a binary search tree, or `None` for an empty tree.

**Return value**

- The native `Codec.serialize(root)` returns an encoded string, and `Codec.deserialize(data)` reconstructs the original tree.
- The app-local `solve` adapter returns the tree produced by serializing and then deserializing `root`.

The standalone app defines a minimal local equivalent of LeetCode's injected `TreeNode` model.
