# Serialize and Deserialize Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 297 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |

## Problem Description
### Goal
Design a codec for arbitrary binary trees. `serialize(root)` must convert the complete tree into a string representation that preserves node values and enough information about missing children to distinguish different shapes that share the same traversal values.

`deserialize(data)` must reconstruct a new tree structurally and numerically identical to the serialized input, including negative or repeated values and unbalanced branches. An empty tree must round-trip correctly. The exact encoding format is yours to choose, but decoding must unambiguously invert every string produced by the encoder. The app adapter performs one complete round trip, while the native `Codec` exposes both operations.

### Function Contract
**Inputs**

- `root`: a `TreeNode`, encoded as a level-order `List[int | null]` in app cases

**Return value**

The root node of the reconstructed tree, normalized back to level-order form by the app judge.

### Examples
**Example 1**

- Input: `root = [1,2,3,null,null,4,5]`
- Output: `[1,2,3,null,null,4,5]`

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [1]`
- Output: `[1]`
