## Function Contract

**Inputs**

- `root`: The binary tree. App-authored cases serialize it in level order, using `null` for a missing child; the local judge deserializes that form into a node tree, matching the `TreeNode` root supplied to the native method.

Let $n$ be the number of non-null nodes. A path follows tree edges and may move through a parent between two branches. Each selected node contributes its value once, and no two selected nodes may have equal values.

**Return value**

Return the maximum sum over every non-empty connected path whose node values are pairwise distinct. A one-node path is valid, so the result remains well-defined when every value is negative.
