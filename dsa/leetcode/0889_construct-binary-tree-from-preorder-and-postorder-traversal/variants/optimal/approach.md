## General
**Locate each subtree's postorder boundary**

The first unused preorder value is the root of the current subtree. If more nodes remain in that subtree, the next preorder value is the root of its first child subtree. Because postorder places a subtree root last, an index map from value to postorder position identifies exactly where that first child subtree ends.

**Recurse over disjoint postorder intervals**

Maintain one advancing `preorder_index`. For a current postorder interval `[left, right]`, create the next preorder value as the root. The position of the following preorder value closes the first child interval, which is constructed as `root.left`. If nodes remain between that interval and the root at `postorder[right]`, construct them as `root.right`.

The chosen root is correct because preorder always visits it first. The next preorder value must begin the first child subtree, and its unique postorder position gives that entire subtree's final element, so the interval split cannot mix nodes from the two children. Recursively applying the same argument produces both required traversals. When only one child exists, assigning it to the left is one of the explicitly permitted answers.

## Complexity detail
Building the postorder index map costs $O(n)$ time. Every node is created once and every interval boundary is found in constant time, so reconstruction also takes $O(n)$ time. The map, returned nodes, and recursion stack use $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Search postorder for every split:** Omitting the index map keeps the same recursion but can cost $O(n^2)$ time on a skewed tree.
- **Slice arrays recursively:** This is concise, but repeated slicing and searches also cause $O(n^2)$ copying and lookup work.
- **Iterative stack construction:** A stack synchronized with postorder can build a valid tree in $O(n)$ time, though the completion condition is less direct.
- **Single node:** The shared value is the root and both children are absent.
- **Single-child ambiguity:** Either left or right placement is valid as long as both traversals remain unchanged.
- **Distinct values:** Uniqueness makes the postorder index map and every subtree boundary unambiguous.
- **Full two-child node:** Nodes after the first child interval and before the current postorder root necessarily form the second child subtree.
