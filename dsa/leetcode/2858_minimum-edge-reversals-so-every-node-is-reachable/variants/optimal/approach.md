## General

**Encode the cost of traversing each edge outward**

Treat the tree as undirected for traversal, but annotate both directions. For an original edge `u -> v`, store `(v, 0)` in `u`'s adjacency list because a tree rooted at `u` can traverse that edge outward without reversing it. Store `(u, 1)` in `v`'s list because traversing from `v` toward `u` requires reversing the original edge.

Root the undirected tree temporarily at node `0`. During one iterative traversal, record each node's parent, traversal order, and the annotated cost of its parent edge. Summing those parent-edge costs gives `answer[0]`: every unique root-to-node path must point away from root `0`, so each cost-one edge must be reversed, every cost-zero edge is already correct, and no other reversals can help.

**Reroot with one local change**

Suppose `child` is adjacent to `parent` in the temporary rooting, and let `cost` describe traversal from `parent` to `child`. Moving the conceptual root across this edge changes no requirement for any other edge: their parent-child orientation stays the same.

If `cost = 0`, the original edge points `parent -> child`. It was correct for the parent root but becomes wrong for the child root, so the answer increases by one. If `cost = 1`, the original edge points `child -> parent`; the parent root counted a reversal, while the child root can now use it unchanged, so the answer decreases by one. Both cases are captured by

`answer[child] = answer[parent] + 1 - 2 * cost`.

Process nodes in the stored parent-before-child order to compute every answer. Since the base count is minimal and each reroot transition accounts exactly for the sole edge whose required orientation changes, all produced counts are minimal.

## Complexity detail

The graph has $n-1$ edges. Building both adjacency directions and performing the base traversal take $O(n)$ time; the reroot pass also takes $O(n)$ time. The adjacency lists, parent data, traversal order, and answer array use $O(n)$ space.

The benchmark uses $n$ as `size` and supplies a legal forward chain. The rerooting solution visits the tree a constant number of times. A correct alternative that independently traverses the whole tree from every possible root performs $O(n^2)$ work, completes all tiers, and fails the scaling verdict.

## Alternatives and edge cases

- **Traversal from every root:** Compute the necessary reversals independently for each node. This is straightforward and correct but costs $O(n^2)$ time.
- **Recursive two-DFS rerooting:** One depth-first search can compute the base result and another can propagate rerooted answers. It has the same asymptotic bounds, but recursion depth can exceed Python's default limit on a long chain.
- **All edges outward from one node:** That node's answer is zero; neighboring roots differ by exactly one.
- **All edges along a chain:** Answers can range from `0` to `n - 1`, so the method must handle accumulated changes across many reroot steps.
- **Independent calculations:** `answer[i]` describes a fresh choice of reversals for root `i`; reversals are not shared between entries.
- **Tree guarantee:** The unique path between two nodes makes each edge's required outward orientation unambiguous. The reroot transition would not be sufficient for a general graph with cycles.
