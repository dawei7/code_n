## General
**Turn the comparison rule into bucket order:** Every Manhattan distance is an integer from $0$ through $D$. Create one bucket for each distance. Enumerate workers in increasing index order and, for each worker, enumerate bikes in increasing index order. Append `(worker_index, bike_index)` to the bucket for that pair's distance. Within any one bucket, this insertion order already matches the required worker-index and bike-index tie breakers.

**Process globally closest pairs first:** Visit buckets from distance zero upward. For every stored pair, assign it only when its worker has no bike yet and its bike has not been used. Otherwise skip it because an earlier pair has already made at least one endpoint unavailable. Stop as soon as all $W$ workers have bikes.

Every available pair appears exactly once, and bucket traversal orders those pairs lexicographically by `(distance, worker_index, bike_index)`. Therefore, the first pair encountered whose endpoints are both available is precisely the pair demanded by the assignment rule at that moment. Recording it and continuing applies the same argument after each assignment, so the final array is exactly the prescribed allocation.

## Complexity detail
Creating all pair records takes $O(WB)$ time and space. Initializing and scanning the distance buckets costs $O(D)$, while each pair is visited at most once. The total time is $O(WB+D)$ and the total auxiliary space is $O(WB+D)$. Under the stated coordinate bounds, $D=1998$, but keeping it explicit describes why bucket ordering is efficient.

## Alternatives and edge cases
- **Sort every pair:** Sorting triples `(distance, worker_index, bike_index)` directly expresses the rule but costs $O(WB\log(WB))$ time and $O(WB)$ space.
- **Priority queue of all pairs:** A min-heap also yields pairs in the required order, but its removals retain the extra logarithmic factor and stale pairs still need to be skipped.
- **Repeated search among available pairs:** Rescanning all unassigned worker-bike pairs before every assignment uses less stored pair data but can require $O(W^2B)$ time.
- **Equal distances:** Worker index is compared before bike index; inserting pairs in nested worker-then-bike order preserves both tie breakers inside a distance bucket.
- **Already assigned endpoint:** A pair is ignored if either its worker or bike is unavailable, even if it precedes all remaining valid pairs in the global order.
- **More bikes than workers:** Unused bikes are expected; processing ends immediately after every worker has one assignment.
- **Single worker:** The nearest bike is chosen, with the smallest bike index resolving equal distances.
