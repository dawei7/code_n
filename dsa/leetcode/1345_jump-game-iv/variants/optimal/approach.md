## General
**View indices as an implicit unweighted graph.** Each array index is a vertex. Its adjacent-index moves and its same-value moves are edges of unit length, so breadth-first search discovers every index using the minimum possible number of jumps. Begin with index `0`, mark indices when enqueuing them, and process the queue in distance order.

**Index the long-distance edges.** Build a map from each value to the list of indices containing that value. When BFS processes index `i`, its possible destinations are `i - 1`, `i + 1`, and the stored list for `arr[i]`. This avoids searching the whole array to find equal values.

**Consume each value bucket once.** After expanding the bucket for `arr[i]`, remove that bucket from the map. Any future index carrying the same value could only revisit the identical destinations, all of which were marked during the first expansion. Removing the bucket therefore preserves every useful route while preventing a large repeated-value group from being scanned once per member. The first discovery of index `n - 1` is optimal because BFS considers all shorter routes first.

## Complexity detail
Building the value map takes $O(n)$ time and space. Each index is enqueued at most once, the two adjacent edges are checked once per processed index, and every same-value bucket is iterated at most once. Total time is therefore $O(n)$, with $O(n)$ auxiliary space for the map, queue, and visited set.

## Alternatives and edge cases
- **Bidirectional breadth-first search:** Searching from both ends can reduce the explored region in practice, but bucket consumption must be coordinated carefully between the two frontiers; the one-direction BFS already meets the required bound.
- **Repeated bucket scans:** Keeping each value list after expansion is correct, but an array with one large repeated group makes it perform $O(n^2)$ work.
- **Single element:** The start is already the destination, so the answer is zero.
- **All values equal:** The last index is reachable in one same-value jump.
- **Negative values:** Values are only hash-map keys; their sign has no effect on connectivity.
