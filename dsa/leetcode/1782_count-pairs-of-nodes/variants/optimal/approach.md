## General
**Count degrees and direct multiplicities separately**

Scanning `edges` provides two related statistics. Increment the degree of both endpoints for every edge, including every parallel copy. At the same time, normalize the endpoint order and count how many edges each distinct pair shares.

The degree sum of two nodes is a useful first estimate, but it double-counts every direct edge between them. The exact incident-edge count is therefore their degree sum minus their shared multiplicity.

**Count qualifying degree sums with two pointers**

Sort a copy of the degree array. For one query, place pointers at its two ends. If the current smallest-plus-largest sum is above the query, pairing the right value with every degree from `left` through `right - 1` also succeeds, contributing `right - left` pairs at once. Move `right` leftward. Otherwise, the left degree cannot succeed with any available partner, so move `left` rightward.

This counts every unordered node pair whose raw degree sum is above the query in linear time after sorting.

**Repair exactly the pairs inflated by their shared edges**

Only node pairs that are themselves connected can disagree between the raw test and the true incident-edge test. Iterate over the $P$ distinct connected pairs. A pair was incorrectly included precisely when its degree sum is above the query but becomes at most the query after subtracting its direct-edge multiplicity. Subtract one for each such pair.

The first pass counts all raw qualifying pairs once, and the repair removes exactly those and only those that fail the actual definition. Thus the remaining count is the requested answer.

## Complexity detail
Building degrees and multiplicities costs $O(E)$ time. Sorting the $n$ degrees costs $O(n\log n)$. Each of the $Q$ queries performs an $O(n)$ two-pointer scan and an $O(P)$ correction pass, giving $O(E + n\log n + Q(n + P))$ total time.

The degree arrays use $O(n)$ space and the multiplicity map stores $P$ entries, for $O(n + P)$ auxiliary space. The output contains $Q$ integers.

## Alternatives and edge cases
- **Binary search for each node:** Sorting also permits finding the first qualifying partner independently for each node. This is correct but costs $O(Qn\log n)$ before the same multiplicity corrections, while two pointers make each query's raw count linear.
- **Enumerate every node pair:** Computing the exact incident count directly is simple and useful as a small-input oracle, but it takes $O(Qn^2)$ time and does not meet the required scaling.
- **Parallel edges:** Every copy increases both endpoint degrees, yet all copies between the selected pair must be subtracted from that pair's degree sum.
- **Disconnected or isolated nodes:** Pairs need not share an edge to qualify; their degrees may come from entirely different components.
- **Strict comparison:** A pair with incident-edge count equal to the query is excluded.
- **Endpoint order:** `[u, v]` and `[v, u]` represent the same unordered endpoint pair when shared multiplicities are counted.
