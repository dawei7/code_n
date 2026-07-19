# Serialize and Deserialize N-ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 428 |
| Difficulty | Hard |
| Topics | String, Tree, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) |

## Problem Description
### Goal
Design a codec for an N-ary tree whose nodes contain values and ordered child lists of arbitrary length. `serialize(root)` must encode the complete hierarchy into one string, including enough boundary information to distinguish siblings, descendants, leaves, and empty child lists.

`deserialize(data)` must reconstruct an equivalent new tree with every value, parent-child relationship, and sibling order preserved. An empty tree must round-trip correctly. The exact encoding format is yours to choose, but it must be unambiguous and cannot depend on global or static state left by another call. The app adapter verifies the full serialize-deserialize round trip.

### Function Contract
**Inputs**

- `tree`: the app representation of an N-ary root as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- Serialize the tree, deserialize that data, and return the reconstructed nested representation. The native LeetCode artifact exposes the required `Codec.serialize(root)` and `Codec.deserialize(data)` methods.

### Examples
**Example 1**

- Input: `tree = [1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`
- Output: `[1, [[3, [[5, []], [6, []]]], [2, []], [4, []]]]`

**Example 2**

- Input: `tree = [7, []]`
- Output: `[7, []]`

**Example 3**

- Input: `tree = None`
- Output: `None`
