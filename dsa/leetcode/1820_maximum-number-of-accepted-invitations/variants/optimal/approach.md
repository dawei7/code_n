## General
**View accepted invitations as a bipartite matching**

Boys form one vertex partition and girls the other; every 1 in `grid` is an edge. An accepted set cannot reuse a vertex, so it is exactly a matching. Store, for each girl, the boy currently matched to her, or `-1` when she is free.

**Search for an augmenting path from every boy**

For one boy, run depth-first search across acceptable girls not yet visited during this attempt. A free girl can be matched immediately. If a girl is occupied, recursively try to move her current boy to another acceptable girl. When that succeeds, assign the newly freed girl to the requesting boy. Use a fresh visited-girl array for each outer attempt so later boys may reconsider paths while cycles within one attempt are avoided.

**Why every successful search increases an optimal matching**

A successful recursion traces an alternating path whose edges switch between unmatched and matched. Reversing their status adds the starting boy and ends at a previously free girl, increasing matching size by one without duplicating any endpoint. If no augmenting path exists from any remaining unmatched boy, the augmenting-path characterization of bipartite matching says the current matching is maximum. Processing every boy therefore returns the largest feasible invitation count.

## Complexity detail
Let $E\le mn$ be the number of 1-cells. One augmenting search visits each girl at most once and scans adjacency rows reached through matched boys, costing $O(E)$ in the worst case. Running it for all $m$ boys costs $O(mE)\subseteq O(m^2n)$. The girl-match array, one visited array, and recursive boy path use $O(m+n)$ space.

## Alternatives and edge cases
- **Choose the first free girl greedily:** It can strand a later boy whose only option was taken; augmenting paths repair exactly this failure.
- **Bitmask dynamic programming:** It is exact for a small number of girls, but its $O(m2^n)$ state space is infeasible when $n$ reaches 200.
- **Maximum-flow network:** Source/boy/girl/sink capacities produce the same answer, but a dedicated bipartite matcher is simpler here.
- **All-zero matrix:** No augmenting search succeeds, so return zero.
- **Rectangular matrix:** The answer is at most $\min(m,n)$; the algorithm does not require equal partition sizes.
- **One girl acceptable to many boys:** At most one of those incident edges can belong to the matching.
- **Reassignment required:** Recursion may move several earlier boys before a free girl is reached.
