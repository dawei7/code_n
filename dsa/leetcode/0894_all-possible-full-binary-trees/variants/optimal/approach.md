## General
**Split the remaining nodes between two full subtrees**

A one-node tree is a valid leaf. Any larger full tree has a root plus nonempty left and right full subtrees. Because full trees have odd sizes, try every odd `left_nodes` from `1` through `nodes - 2`; the right size is `nodes - 1 - left_nodes` and is also odd.

**Memoize every subtree size**

For each size split, recursively obtain all left shapes and all right shapes. Their Cartesian product supplies every pair of children for a new abstract root shape. Cache the immutable shape list produced for each node count so the same subtree-size family is generated only once. Finally, materialize each complete shape as a fresh tree of zero-valued nodes.

Every constructed root has two full children, so it is full and has exactly the requested number of nodes. Conversely, take any full tree with more than one node. Its left subtree has some odd size considered by the loop, its right subtree has the complementary size, and by induction both shapes appear in the cached recursive results; their pair therefore constructs that tree. Different ordered child-shape pairs produce different binary-tree structures, so the algorithm returns every possibility without structural duplicates.

## Complexity detail
There are $F(n)$ output shapes, each containing $n$ logical nodes. Constructing and representing the complete result therefore takes $O(nF(n))$ time and space in the output-sensitive bound. Memoization avoids regenerating the same smaller size families; its retained subtree roots and recursion depth fit within the same $O(nF(n))$ bound.

## Alternatives and edge cases
- **Recurse without memoization:** The same split recurrence is correct but repeatedly rebuilds identical subtree-size families and adds substantial redundant work.
- **Bottom-up dynamic programming:** Filling lists for odd sizes from `1` through `n` applies the same Cartesian products iteratively with equivalent output-sensitive bounds.
- **Generate arbitrary trees and filter:** Enumerating non-full binary trees first creates a much larger search space and discards most candidates.
- **Even node count:** Return an empty list because every full tree has one root plus pairs of descendants and therefore odd total size.
- **One node:** The sole result is a leaf with value `0`.
- **Ordered children:** Swapping unequal left and right shapes creates a distinct binary tree and both orientations must be included.
- **Mutable node aliasing:** Cache immutable shapes rather than `TreeNode` instances, then create fresh nodes for each returned root so no result accidentally shares a mutable node with another branch or tree.
