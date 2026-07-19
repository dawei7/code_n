## General
**Use the root as the reference.** Since the tree is nonempty, store `root.val` before traversal. Every node must equal this single value; no frequency table or ordering property is needed.

**Traverse each existing node once.** Maintain a depth-first stack beginning with `root`. Pop a node, return `false` immediately if its value differs from the reference, and push each non-null child. If the traversal finishes without finding a mismatch, every node has been checked and the tree is uni-valued.

**Why early rejection is safe.** One differing node is enough to violate the definition, regardless of values elsewhere. Conversely, reaching the end proves that every node belongs to the visited set and matched `root.val`, so returning `true` is sufficient and necessary.

## Complexity detail
Each of the $N$ nodes is pushed, popped, and compared once, giving $O(N)$ time. A depth-first traversal retains at most $O(H)$ pending nodes, so auxiliary space is $O(H)$.

## Alternatives and edge cases
- **Recursive depth-first search:** Require the current node to match the root and recursively validate both children. This is equally direct but uses the language call stack.
- **Breadth-first search:** A queue also checks every node in $O(N)$ time, but its space is the maximum tree width rather than the height.
- **Repeated subtree scans:** Recheck every descendant for each possible subtree root. This remains correct but can take $O(N^2)$ time on a chain.
- **Single node:** A one-node tree is uni-valued by definition.
- **Zero value:** `0` is a valid node value and must not be treated as a missing node.
- **Sparse shape:** Missing children do not affect the result; only existing node values matter.
