## General
**Attach queries to their tree nodes**

Build child lists from `parents` and group each query with its target node,
retaining the query's original index. This lets a single tree traversal answer
queries exactly when their complete ancestor path is known.

**Maintain the active root-to-node path**

Traverse the tree depth first. On entering a node, insert its numeric label
into a counted binary trie. At that moment, the trie contains precisely the
queried node and all of its ancestors: earlier sibling subtrees have already
been removed, while descendants have not yet been entered. Answer every query
attached to the node, then visit its children. On leaving the node, decrement
its trie counts.

Use explicit enter and exit events on a stack rather than recursive calls, so
a chain of up to $10^5$ nodes cannot overflow Python's recursion limit.

**Choose opposite bits greedily**

For a query value, walk the trie from the highest bit downward. At each bit,
prefer an active branch whose bit is opposite the query bit, because that sets
the current result bit to one. If no counted node exists on that branch, take
the matching branch. Higher XOR bits dominate every combination of lower
bits, so this greedy choice yields the maximum XOR among all active ancestors.

The DFS path invariant restricts candidates to exactly the permitted nodes,
and the trie walk maximizes against that set. Storing results by original query
index preserves input order even though queries are processed in traversal
order.

## Complexity detail
Each node label is inserted once and removed once, with $B$ trie steps per
operation. Each of the $Q$ queries also takes $B$ steps, giving
$O((N+Q)B)$ time. The child lists and grouped queries use $O(N+Q)$ space, and
the trie can contain $O(NB)$ nodes across all inserted labels. The traversal
stack uses $O(N)$ space, so the total is $O(NB+Q)$.

## Alternatives and edge cases
- **Walk parents for every query:** Check the target and repeatedly follow
  `parents` to the root. This is simple and correct, but a chain with a query
  at every node takes $O(NQ)$ time.
- **Persistent trie per node:** Derive each node's trie version from its
  parent's version. Queries are fast and online, but persistence stores
  $O(NB)$ nodes and is more involved than the reversible DFS trie.
- The queried node and root are both eligible candidates.
- The root may have any node index; it is identified by its `-1` parent rather
  than assumed to be node zero.
- Queries on different branches must not see sibling or cousin labels.
- Multiple queries attached to one node share the same active trie but retain
  separate answers and order.
- A query value of zero asks for the numerically largest ancestor label.
- The bit width must cover query values as well as node labels.
