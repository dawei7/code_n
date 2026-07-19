## General
**Carry the prefix value down the tree:** At a node, append its bit to the binary prefix with `current = current * 2 + node.val`. Pass that value to both children rather than storing the path as characters.

**Contribute only at leaves:** If a node has neither child, the current prefix is one complete root-to-leaf number, so return it. Otherwise recursively sum the contributions of the existing left and right subtrees.

**Why prefixes can be shared:** Both child paths have exactly the same bits through their parent. Computing that prefix once and extending it independently avoids rebuilding common path segments for each leaf.

By induction on path length, `current` at every node equals the binary value from the root through that node. Each leaf is visited exactly once and contributes its represented number, so the accumulated total is precisely the requested sum.

## Complexity detail
The traversal visits each of the $N$ nodes once and performs constant work per node, giving $O(N)$ time. Recursion follows one root-to-leaf path at a time and uses $O(H)$ call-stack space.

## Alternatives and edge cases
- **Find every leaf path independently:** Searching again from the root for each leaf repeats shared traversal work and can take $O(N^2)$ time.
- **Iterative stack:** Storing `(node, prefix)` pairs avoids recursion while retaining $O(N)$ time and $O(H)$ space on a depth-first traversal.
- **Single node:** Its bit is the only path value.
- **Leading zero:** It contributes no extra value but remains part of the path structure.
- **Missing child:** Continue only through existing nodes; a node is a leaf only when both children are absent.
