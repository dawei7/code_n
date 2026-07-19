## General
**Inorder still provides the subtree boundaries**

Map every distinct value to its unique inorder index. Once a root is known, that index divides the current interval into exactly the keys of its left and right subtrees, with no scanning or copied slices.

**Reverse postorder exposes root, then right subtree, then left**

Postorder is left-right-root. A cursor moving backward sees root-right-left. Consume the current postorder value as the root, recursively build its right inorder interval, and only then build its left interval. Reversing this recursive order would consume right-subtree values while trying to place them in the left interval.

An empty interval returns null without moving the shared cursor.

**The backward cursor consumes exactly one interval's nodes**

On entry to `build(left,right)`, the postorder cursor points to that interval's root. The call consumes exactly its number of nodes in reverse postorder and returns the unique tree over those inorder positions. On exit, the cursor points to the root of the next unbuilt interval.

**Trace why the right child must be built first**

The last value `3` is the root and splits inorder into `[9]` and `[15, 20, 7]`. Reading backward next reaches root `20`; building its right child `7` before its left child `15` respects reverse postorder, then node `9` completes the left side.

**Reverse postorder exposes the right subtree before the left**

The last value of any postorder subtree segment is its root. Its unique inorder position separates exactly the left and right subtree values. Reading postorder backward visits root, then the right subtree's reversed segment, then the left subtree's.

Constructing right before left therefore consumes values in their required reverse-postorder order. Applying the same unique root-and-partition argument recursively rebuilds both children and the only tree compatible with the traversals.

## Complexity detail
Building the index map takes $O(n)$ time, and every node is created once with constant-time lookup, so total time is $O(n)$. The map, output nodes, and recursion stack use $O(n)$ space; recursion itself is $O(h)$ deep.

## Alternatives and edge cases
- **Search inorder for each root:** becomes $O(n^2)$ on skewed inputs.
- **Copy array slices recursively:** adds repeated allocation and can become quadratic.
- **Build left before right while reading backward:** consumes nodes in the wrong order and constructs an incorrect tree.
- Empty traversals produce an empty tree. Distinct values make each inorder split unique.
- The approach assumes both traversals describe the same valid tree; input consistency validation is outside the stated contract.
