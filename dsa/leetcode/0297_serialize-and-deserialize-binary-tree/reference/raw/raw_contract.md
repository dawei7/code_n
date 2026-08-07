## Function Contract

**Inputs**

- `root`: A binary-tree root, represented by a level-order list with `null` placeholders in app cases.

**Return value**

The app adapter serializes `root`, deserializes the resulting string, and returns the reconstructed root for level-order comparison. The native `Codec` exposes separate `serialize(root)` and `deserialize(data)` operations.
