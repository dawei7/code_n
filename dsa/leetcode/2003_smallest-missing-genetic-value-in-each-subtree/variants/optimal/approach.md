## General
**Identify the only subtrees that can exceed one.** If the tree has no node carrying genetic value $1$, every answer is immediately $1$. Otherwise, a subtree can contain $1$ only when its root is the node holding $1$ or one of that node's ancestors. Initialize every answer to $1$ and process only this ancestor path.

**Grow the covered subtree while walking upward.** Build children lists and start at the node whose value is $1$. For the current path node, traverse its subtree and add genetic values from nodes not visited during an earlier step. Then move to its parent. The previously covered subtree remains included, while the traversal adds precisely the parent's value and any sibling branches. A visited array ensures each tree node is incorporated at most once.

**Maintain the missing value monotonically.** Keep a set of all values incorporated so far and a pointer `missing`, initially $1$. After each expansion, advance the pointer while it belongs to the set, then assign it to the current path node. The covered values are exactly that node's subtree, so the first absent positive value is correct. Moving upward only adds values, so `missing` never needs to decrease and advances at most $N+1$ times overall.

## Complexity detail
Building child lists takes $O(N)$ time and space. Across every incremental traversal, each node is marked and its children are expanded once. The missing-value pointer advances monotonically, so all path steps together take $O(N)$ time. Children, visited flags, the value set, and the answer use $O(N)$ space.

## Alternatives and edge cases
- **Traverse every subtree independently:** Collecting values and finding the missing positive for each root can take $O(N^2)$ time on a chain.
- **Merge a set from every child:** Small-to-large set merging can solve the general subtree problem in $O(N\log N)$ time, but does not exploit the special role of genetic value $1$.
- If value $1$ is absent from the entire tree, every answer is $1$.
- Nodes outside the ancestor path of value $1$ cannot have an answer larger than $1$.
- When value $1$ is at the root, only the root needs a nontrivial computation.
- Distinct genetic values eliminate multiplicity concerns when values are added to the global set.
