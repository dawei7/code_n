# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1379 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) |

## Problem Description

### Goal

A binary tree has been copied exactly. The root of the source tree is `original`, and `cloned` is the root of the separate cloned tree with the same structure and node values. A particular node object inside the source tree is supplied as `target`.

Return the node object in the cloned tree that occupies the same structural position as `target` occupies in the original. The answer must be a reference to the existing cloned node; do not modify either tree, and do not rely on node values being unique.

### Function Contract

**Inputs**

- `original`: the root node of the original binary tree containing $N$ nodes.
- `cloned`: the root node of a distinct tree that is an exact clone of `original`.
- `target`: a tree node object that belongs to the original tree.

**Return value**

- The existing tree node in `cloned` corresponding to the exact object `target` in `original`.

### Examples

**Example 1**

- Input: `original = [7,4,3,null,null,6,19], target = node 3`
- Output: `node 3 in cloned`

**Example 2**

- Input: `original = [7], target = node 7`
- Output: `node 7 in cloned`

**Example 3**

- Input: `original = [8,null,6,null,5,null,4], target = node 6`
- Output: `node 6 in cloned`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Traverse both trees in lockstep.** Put the pair `(original, cloned)` on an explicit stack. Each pair always contains nodes at the same structural position because the two roots correspond and matching left or right children are pushed together.

For every pair, compare the original-side node with `target` by object identity. When they are the same object, return the clone-side node from that pair. Otherwise continue with the matching child pairs. Since `target` is guaranteed to belong to the original tree, one visited pair must match.

The lockstep invariant proves the returned object is at precisely the target's position in the clone. Identity comparison also remains correct when two or more nodes share the same value, whereas a value-only search could return the wrong occurrence.

#### Complexity detail

In the worst case the traversal examines all $N$ corresponding node pairs, so time is $O(N)$. The explicit stack contains at most $O(N)$ pairs in the worst case.

#### Alternatives and edge cases

- **Record and replay the target path:** Find the root-to-target directions in the original and follow them in the clone. This is also $O(N)$ time, but requires path bookkeeping.
- **Build every node's path independently:** Repeatedly replay root paths in the clone. It is correct but can take $O(N^2)$ time on a chain.
- **Match by value:** This works only when values are unique and is invalid for the general identity-based contract.
- **Target is the root:** The corresponding answer is immediately the `cloned` root.
- **Duplicate values:** Compare original node objects with `is`, not their `val` fields.
- **Deep tree:** The iterative stack avoids recursion-depth failure on a skewed tree.
- **Existing object required:** Return a node already reachable from `cloned`, never a newly allocated copy.

</details>
