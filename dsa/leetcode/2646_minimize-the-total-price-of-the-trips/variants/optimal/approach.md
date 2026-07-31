## General

First aggregate how often every node is used. For each trip, find its unique tree path and increment `usage` for every node on that path. Node $u$ then contributes `usage[u] * price[u]`, or half that amount when discounted.

Root the tree arbitrarily and compute two subtree costs. When $u$ remains full, each child may use its cheaper state. When $u$ is halved, every child must remain full because adjacent discounts are forbidden. These transitions consider every legal independent set in each subtree, so the cheaper root state is globally optimal.

## Complexity detail

Let $t$ be the number of trips. Each path search visits at most $n$ nodes, giving $O(nt)$ time for aggregation; the tree DP adds $O(n)$ time. The adjacency list, usage array, and recursion stacks use $O(n)$ space.

## Alternatives and edge cases

- **LCA difference accumulation:** This improves path aggregation for larger limits but adds unnecessary machinery when $n \le 50$.
- **Exhaustive discount subsets:** Testing every independent subset is correct but exponential in $n$.
- **Per-trip discounts:** Choosing discounts separately for each trip violates the one-time global choice.
- A self trip uses exactly one node.
- Unused nodes contribute zero in either DP state.
- Even prices guarantee integral halving.
