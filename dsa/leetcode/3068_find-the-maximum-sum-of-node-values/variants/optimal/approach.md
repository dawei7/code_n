## General

**Reduce edge operations to an even-parity choice.** Each operation XORs exactly two nodes, so every reachable final state has an even number of nodes whose values were toggled an odd number of times. The tree's connectivity makes the converse true as well. To toggle any chosen pair of nodes, operate on every edge along their unique path: the endpoints are toggled once, while each internal node is toggled twice and returns to its original value. Pairing the nodes of any even-sized chosen set therefore realizes that set. The particular tree shape no longer affects the optimum beyond guaranteeing connectivity.

**Take every node's locally better value first.** For a value `value`, compare it with `value ^ k` and add the larger one to a provisional total. Count how many of those local choices use the toggled value. If this count is even, the provisional choices form a reachable state and no other state can have a larger sum because every node already contributes its individual maximum.

**Repair an odd choice with the cheapest change.** If the number of beneficial toggles is odd, one node must switch away from its locally preferred state. For each node, the cost of switching that choice is `abs((value ^ k) - value)`. Subtract the smallest such cost from the provisional total. This covers both possibilities—reverting a beneficial toggle or adding a non-beneficial toggle—and yields the best reachable even-parity selection.

Every returned selection has even parity, hence is realizable by path operations. When the provisional toggle count is odd, every feasible selection must disagree with at least one local maximum; the algorithm chooses the least expensive possible disagreement. Thus no feasible sum can exceed the returned one.

## Complexity detail

Let $n$ be the number of nodes. One pass over `nums` computes the provisional sum, parity, and smallest adjustment in $O(n)$ time. The algorithm uses only scalar accumulators, so its auxiliary space is $O(1)$. The `edges` array need not be traversed because the valid-tree guarantee already establishes connectivity.

## Alternatives and edge cases

- **Two-state parity dynamic programming:** Track the best sum after each prefix with an even or odd number of toggles. This is also $O(n)$ time and $O(1)$ space, but the greedy parity repair expresses the same choice more directly.
- **Sort all XOR gains:** Sorting gains can identify the best even-sized prefix in $O(n \log n)$ time, which is unnecessary when only the smallest parity adjustment matters.
- **Tree dynamic programming:** A subtree DP can model edge operations explicitly, but it retains tree structure that collapses to the global even-parity invariant.
- **No beneficial toggles:** The provisional toggle count is zero and the original sum is returned.
- **Odd beneficial count:** Exactly one local choice must be reversed; the cheapest absolute gain or loss is the complete parity correction.
- **Two nodes:** The only reachable toggle counts are zero and two, both handled by the parity rule.
- **Large sum:** Although each value is at most $10^9$, the answer can exceed 32-bit range because as many as $2 \cdot 10^4$ values are added.
- **Tree shape:** A path, star, or any other valid tree permits the same even subsets through unique-path operations.
