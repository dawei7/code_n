## General

**Root each candidate path at its highest node**

Relative to root `0`, every simple path has one node closest to the root. From
that highest node, the path can descend into at most two child subtrees: one
branch toward each endpoint. This makes each node a possible meeting point for
two downward chains.

**Summarize a subtree by one downward chain**

For every node, compute the longest valid chain that begins there and descends
within its subtree. A child's chain can extend the current node only when
`s[child] != s[node]`; otherwise their connecting edge violates the adjacent-
character condition. Among compatible children, the longest chain determines
the downward summary returned to the parent.

For a complete path whose highest node is the current node, keep the two
largest compatible child-chain lengths. Joining those chains through the
current node produces a candidate of `first + second + 1` nodes. No other
child branch can belong to the same simple path, and choosing the two largest
maximizes this candidate. Every valid path is considered at its highest node,
so the greatest candidate is the answer.

**Use an explicit postorder**

Build child lists, traverse iteratively from the root to record a parent-before-
child order, then process that order backward. Every child's downward value is
therefore ready before its parent. This avoids recursion-depth failure on a
legal chain of $10^5$ nodes.

## Complexity detail

Let $n=\lvert\texttt{parent}\rvert$. Building child lists, producing the
traversal order, and scanning every child edge during the bottom-up pass each
take $O(n)$ time. Child lists, traversal order, stack, and downward lengths use
$O(n)$ space.

## Alternatives and edge cases

- **Start a search from every endpoint:** Recomputing paths from every node is correct but can take $O(n^2)$ time.
- **Recursive depth-first search:** It expresses the same recurrence, but a chain of $10^5$ nodes can exceed Python's recursion limit.
- **Keep only the longest child chain:** That suffices for the value passed upward but misses paths joining two child subtrees through the current node.
- **Compare all characters on a path:** Only adjacent pairs are constrained; equal nonadjacent characters are allowed.
- **Equal parent-child characters:** Ignore that edge for valid-chain extension, while still processing the child's subtree independently.
- **Single node:** A path containing only the root is valid and has length `1`.
- **All characters equal:** Every edge is unusable, so the answer remains `1`.
- **Path need not include root:** The global maximum is updated at every node, including nodes deep in the tree.
