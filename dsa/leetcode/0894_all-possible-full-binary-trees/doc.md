# All Possible Full Binary Trees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 894 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Tree, Recursion, Memoization, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/all-possible-full-binary-trees/) |

## Problem Description
### Goal
A full binary tree is a binary tree in which every node has either exactly zero children or exactly two children. Every node in this problem must store the value `0`.

Given `n`, construct all structurally distinct full binary trees containing exactly `n` nodes. Return a list of their root nodes in any order. Each returned root represents one possible tree shape; when no full binary tree can contain `n` nodes, return an empty list.

### Function Contract
Let $F(n)$ be the number of full binary tree shapes with $n$ nodes. For odd $n=2m+1$,

$$
F(n)=\frac{1}{m+1}\binom{2m}{m},
$$

and $F(n)=0$ for even $n$.

**Inputs**

- `n`: the required number of nodes, where $1 \leq n \leq 20$.

**Return value**

Return the roots of all $F(n)$ structurally distinct full binary trees with `n` nodes and value `0` at every node; the root-list order is unrestricted.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]`

**Example 2**

- Input: `n = 3`
- Output: `[[0,0,0]]`

**Example 3**

- Input: `n = 2`
- Output: `[]`

A full binary tree always has an odd number of nodes.

### Required Complexity
- **Time:** $O(nF(n))$
- **Space:** $O(nF(n))$

<details>
<summary>Approach</summary>

#### General

**Split the remaining nodes between two full subtrees**

A one-node tree is a valid leaf. Any larger full tree has a root plus nonempty left and right full subtrees. Because full trees have odd sizes, try every odd `left_nodes` from `1` through `nodes - 2`; the right size is `nodes - 1 - left_nodes` and is also odd.

**Memoize every subtree size**

For each size split, recursively obtain all left shapes and all right shapes. Their Cartesian product supplies every pair of children for a new abstract root shape. Cache the immutable shape list produced for each node count so the same subtree-size family is generated only once. Finally, materialize each complete shape as a fresh tree of zero-valued nodes.

Every constructed root has two full children, so it is full and has exactly the requested number of nodes. Conversely, take any full tree with more than one node. Its left subtree has some odd size considered by the loop, its right subtree has the complementary size, and by induction both shapes appear in the cached recursive results; their pair therefore constructs that tree. Different ordered child-shape pairs produce different binary-tree structures, so the algorithm returns every possibility without structural duplicates.

#### Complexity detail

There are $F(n)$ output shapes, each containing $n$ logical nodes. Constructing and representing the complete result therefore takes $O(nF(n))$ time and space in the output-sensitive bound. Memoization avoids regenerating the same smaller size families; its retained subtree roots and recursion depth fit within the same $O(nF(n))$ bound.

#### Alternatives and edge cases

- **Recurse without memoization:** The same split recurrence is correct but repeatedly rebuilds identical subtree-size families and adds substantial redundant work.
- **Bottom-up dynamic programming:** Filling lists for odd sizes from `1` through `n` applies the same Cartesian products iteratively with equivalent output-sensitive bounds.
- **Generate arbitrary trees and filter:** Enumerating non-full binary trees first creates a much larger search space and discards most candidates.
- **Even node count:** Return an empty list because every full tree has one root plus pairs of descendants and therefore odd total size.
- **One node:** The sole result is a leaf with value `0`.
- **Ordered children:** Swapping unequal left and right shapes creates a distinct binary tree and both orientations must be included.
- **Mutable node aliasing:** Cache immutable shapes rather than `TreeNode` instances, then create fresh nodes for each returned root so no result accidentally shares a mutable node with another branch or tree.

</details>
