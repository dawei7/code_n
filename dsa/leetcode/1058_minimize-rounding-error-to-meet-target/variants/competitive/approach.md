## General
Given an array of `prices` `[p_1,p_2...,p_n]` and a `target`, round each price $p_{i}$ to $\text{Round}_{i}(p_{i})$ so that the rounded array `[Round_1(p_1),Round_2(p_2)...,Round_n(p_n)]` sums to the given `target`. Each op..., the algorithm executes a two-pointer approach to shrink boundaries or maintain a sliding window. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(N+K)$ — Operation count bound.
- **Space Complexity**: $O(K)$ — Auxiliary memory allocation bound.
