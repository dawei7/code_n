## Function Contract

**Inputs**

- `root`: The root node of a non-empty binary tree. Each node has an integer `val` and optional `left` and `right` children.

For each complete tree level, use left-to-right node order when its one-based level number is odd and right-to-left order when it is even. Stop that level's sum before the first node without the required directional child: `left` on odd levels and `right` on even levels.

**Return value**

Return the level sums from the root level through the deepest level. A level contributes `0` when its first inspected node already lacks the required child.
