## General
**Treat the list as a pattern.** Copy the linked-list values into an array and build its KMP prefix table. State $k$ means that the current downward path ends with the first $k$ pattern values.

**Precompute every value transition.** For each state from $0$ through $L-1$ and each legal node value, determine the next KMP state. A matching value advances to $k+1$. A mismatch at state zero remains zero; at a later state it reuses the already-built transition from the prefix-table fallback state. Because fallback states are smaller, every required row already exists.

**Carry one state down each tree edge.** Traverse the tree iteratively with pairs of a node and its parent's KMP state. Look up the node value's next state. Reaching $L$ proves a complete list match; otherwise push both children with that new state.

KMP state always represents the longest pattern prefix that is a suffix of the current root-to-node path. The transition table preserves this invariant after every node, including overlapping partial matches. Therefore reaching state $L$ is equivalent to finding the requested contiguous downward path, while visiting every node covers all possible endpoints.

## Complexity detail
Reading the list and building its prefix table takes $O(L)$ time. The deterministic table has $LU$ entries and is built in $O(LU)$ time. Each of the $N$ tree nodes performs one constant-time transition, so total time is $O(N+LU)$. The table uses $O(LU)$ space and the depth-first stack uses $O(H)$ space.

## Alternatives and edge cases
- **Restart DFS at every node:** Attempt to match the list independently from each possible start. This is simple and correct but can take $O(NL)$ time on repeated values.
- **KMP fallback without a table:** Carry a prefix length and follow failure links at each tree node. Branching can repeat the same fallback work; memoized or precomputed transitions make the bound explicit.
- **Recursive traversal:** It mirrors the tree definition but may exceed the language recursion limit on a legal deep tree.
- **Overlapping prefix:** After a mismatch, retain the longest suffix that is also a pattern prefix rather than resetting unconditionally.
- **Single list node:** Any tree node with the same value immediately completes the match.
- **Sibling values:** Two siblings cannot supply consecutive list nodes because the path must move from parent to child.
- **Deep start:** State transitions allow a match to begin at any node without launching a separate search.
