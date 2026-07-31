## General

**Build from the palindrome's center.** Every odd-length palindrome has one central node, so initialize a state for each singleton. Every even-length palindrome has a central edge whose two endpoint labels match, so initialize every such edge as a two-node state. A state consists of a visited-node bitmask and the two current path endpoints. Endpoint order is irrelevant in an undirected graph because reversing a palindrome produces the same valid path.

**Add matching nodes at both ends.** From state `(mask, left, right)`, choose an unvisited neighbor `x` of `left` and a different unvisited neighbor `y` of `right`. The larger path remains palindromic exactly when `label[x] == label[y]`. Adjacency and per-character node sets are bitmasks, so the implementation intersects them before enumerating candidate endpoint pairs. Canonicalize the two new endpoints and memoize the encoded `(new_mask, endpoint_a, endpoint_b)` state.

Every generated state represents a simple path because the new endpoint bits are distinct and absent from `mask`; adjacency connects them to the old ends; and their equal labels wrap an already palindromic sequence. Conversely, repeatedly removing the equal outer labels from any palindromic simple path eventually reaches either its one-node center or its equal-label central edge. Reversing those removals is exactly one sequence of generated transitions, so no valid palindromic path is omitted. The largest visited-mask population is therefore the answer.

**Complete-graph shortcut.** In a complete graph, any ordering of distinct nodes is a valid path. A multiset of labels can be permuted into a palindrome when at most one count is odd. Keep all nodes when that holds; otherwise discard one node from every odd-count label except one. This avoids exploring the densest state space while preserving the general DP for all other graphs.

## Complexity detail

There are at most $2^n n^2$ distinct `(mask, left, right)` states. In the worst case a state considers $O(n)$ unused neighbors at each endpoint, or $O(n^2)$ matching pairs. The conservative worst-case time bound is therefore $O(2^n n^4)$, and the queue plus memoized states use $O(2^n n^2)$ space. Bitmask intersections and endpoint canonicalization reduce constants substantially for $n \le 14$.

The benchmark defines $S=2^n$ and uses a nearly complete graph whose labels prevent a full-length palindrome. The endpoint-mask DP remains exponential in `n` with a polynomial factor, while a calibrated exhaustive simple-path enumeration grows factorially.

## Alternatives and edge cases

- **Enumerate every simple path:** Testing every path's label sequence is correct but can require $\Theta(n!)$ path prefixes in a dense graph.
- **Track only endpoints:** Without the visited mask, an expansion can reuse a node and violate the simple-path condition.
- **Start only from nodes:** That finds odd-length palindromes but misses even-length paths; matching-label edges are also required centers.
- **Equal outer labels:** Both newly added endpoints must match each other, not the old endpoint labels.
- **Distinct new endpoints:** The same unused node cannot be attached to both ends in one transition.
- **No matching edge labels:** Single nodes still yield the valid minimum answer `1`.
- **Disconnected regions:** Each initialized center expands only within edges it can follow; the global maximum may come from any component.
- **Complete graph:** Label multiplicities alone determine the best length because every node order is a valid path.
