## General

Fix a candidate capability $C$. Under this limit, a house is eligible exactly when its value is at most $C$. The remaining question is whether at least `k` eligible houses can be selected without taking adjacent indices.

Scan from left to right. Whenever the current house is eligible, take it and skip the next house; otherwise advance by one. Taking the earliest eligible house is never worse than postponing the choice: it leaves every later index available at least as early as any alternative choice would. This greedy scan therefore produces the maximum number of non-adjacent eligible houses for the threshold.

Feasibility is monotone. If $C$ allows `k` houses, every larger threshold does too; if it does not, every smaller threshold also fails. Binary-search the inclusive value interval from `min(nums)` to `max(nums)`. A feasible midpoint becomes the new upper bound, while an infeasible midpoint moves the lower bound above it. When the bounds meet, they identify the smallest feasible capability.

Although the contract permits robbing more than `k` houses, only feasibility matters. Any valid selection of more than `k` houses can discard extras without increasing its maximum, so finding whether at least `k` can be taken is sufficient.

## Complexity detail

Let $n$ be the number of houses and let $V=\max(\texttt{nums})-\min(\texttt{nums})+1$ be the searched value range. Each feasibility check scans the array in $O(n)$ time, and binary search performs $O(\log V)$ checks, for $O(n\log V)$ time overall. The scan and search use only scalar variables, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over every capability:** A house-robber recurrence can test one threshold, but repeating it for candidate values without binary search wastes the monotone structure.
- **Enumerate thresholds one by one:** Increasing capability from the minimum until feasible is correct but can require $O(nV)$ time when values span a large range.
- **Sort houses by value:** Processing houses from cheapest upward requires maintaining non-adjacent selection feasibility under index activations, which is substantially more complex than the monotone scan.
- **Equal house values:** The search range collapses immediately, and that common value is the answer.
- **One required house:** The minimum array value is optimal because adjacency is irrelevant for a single selection.
- **Adjacent eligible houses:** Greedily taking the left one and skipping the right one preserves the maximum possible count.
- **Maximum feasible `k`:** When `k` is $\lceil n/2 \rceil$, the threshold may be forced by an alternating set that includes a large value.
