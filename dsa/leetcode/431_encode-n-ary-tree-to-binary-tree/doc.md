# Encode N-ary Tree to Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 431 |
| Difficulty | Hard |
| Topics | Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) |

## Problem Description
### Goal
Design a codec that maps an N-ary tree, whose nodes may have any number of ordered children, into a binary tree. The binary representation must retain every value and enough structural information to distinguish parent-child relationships from sibling order.

`encode(root)` returns the binary representation, and `decode(data)` must reconstruct an N-ary tree equivalent to the original. Empty trees must map back to empty trees, leaves must remain leaves, and children must reappear in their original order. The particular reversible convention is implementation-defined, but the round trip cannot omit nodes or rely on external state.

### Function Contract
**Inputs**

- `tree`: the app representation of an N-ary node as `[value, children]`, recursively, or `None` for an empty tree

**Return value**

- Encode the N-ary structure as a binary structure, decode it, and return the reconstructed nested representation. The native artifact exposes the required `Codec.encode(root)` and `Codec.decode(data)` methods.

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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Store the first child on the binary left link**

For each N-ary node, create a binary node with the same value. Recursively encode its children in their existing order. Attach the first encoded child through `left`; this link means “first child,” not an ordered binary-search relation.

**Chain later children through right links**

Keep the previously encoded child and attach each next sibling through `previous.right`. The binary `right` chain therefore records the complete ordered sibling list. Advancing a tail pointer avoids rescanning siblings already linked.

**Decode the two link meanings symmetrically**

Create an N-ary node from the binary value. Start at its `left` child, recursively decode each binary node encountered, append it to the child list, and follow `right` to the next sibling. Apply the same rule recursively within every child.

**Why the mapping is reversible**

Encoding maps exactly one N-ary node to one binary node. Its ordered child list becomes exactly one left edge followed by a right-sibling chain. Decoding interprets those same links with the inverse meanings, so induction over each subtree restores its value and ordered children. No structural choice is ambiguous.

#### Complexity detail

Encoding and decoding each visit all `n` nodes once, giving $O(n)$ time. Recursive calls follow the structural height; excluding the required encoded and decoded objects, auxiliary space is $O(h)$.

#### Alternatives and edge cases

- **Child-count serialization inside binary nodes:** could store explicit metadata but violates the intended use of the existing binary-node fields.
- **Search from the first child for every appended sibling:** remains correct but can take $O(n^2)$ time for one wide child list.
- **Empty structure:** both directions return `None`.
- **Leaf node:** its binary `left` link is `None` and decoding yields an empty child list.
- **Sibling order:** the right chain must follow the original child order exactly.
- **Repeated calls:** the codec must not retain a tail pointer or node mapping between invocations.

</details>
