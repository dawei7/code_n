## General

Treat every array index as a graph node. From index `i`, edges lead to `i - 1`, `i + 1`, and every other index holding the same value. Every edge represents one jump and therefore has equal cost. Breadth-first search is the natural way to find the minimum number of equal-cost edges from index zero to the last index.

The challenge is handling equal-value edges efficiently. If the array contains the same value many times, repeatedly scanning all of its positions from every matching index could become quadratic. The checked-in solution groups equal values once and removes each group after its first expansion.

**Precompute equal-value destinations**

`g = defaultdict(list)` maps each array value to all indices where that value occurs. The loop over `enumerate(arr)` appends every index to exactly one list.

For example, if a value occurs at indices one, two, and seven, `g[value]` is `[1, 2, 7]`. From any one of these nodes, all three list entries represent same-value jump destinations, although the current index itself will later be rejected as already visited.

This preprocessing avoids searching the full array whenever BFS needs equal-value neighbors.

**Process one shortest-distance layer at a time**

The queue starts with index zero, the visited set starts with zero, and `ans` starts at zero. At the beginning of each outer iteration, every index currently in `q` is reachable in exactly `ans` jumps.

The expression `for _ in range(len(q))` captures the current layer size before new nodes are appended. It processes exactly that many nodes. Any newly discovered neighbor goes to the back of the queue and waits for the next layer, where its distance will be `ans + 1`.

When a popped index equals `len(arr) - 1`, BFS has reached the target. Because layers are processed in increasing distance, no later path can use fewer jumps, so returning `ans` is optimal. For a one-element array, zero is already the last index and the method returns zero on the first pop.

**Enumerate all three neighbor types**

The tuple `(i + 1, i - 1, *g.pop(arr[i], []))` combines the right neighbor, left neighbor, and every index sharing `arr[i]`. The starred expression expands the value’s list into the tuple.

Each candidate `j` must lie inside the array and not yet be visited. A valid new node is appended and immediately added to `vis`. Marking it at enqueue time is important: if several current-layer nodes can reach the same destination, only the first enqueue occurs, preventing duplicate work while preserving its shortest distance.

**Why deleting an equal-value group is safe**

`g.pop(arr[i], [])` returns the complete list for the current value and deletes its dictionary entry. Later nodes with that same value receive the empty default list.

The first time BFS processes any index with value `x`, its distance is minimal among all unprocessed nodes. Every index holding `x` is then considered as a one-jump neighbor and, unless already visited through an even shorter route, is enqueued at the earliest possible next distance. Expanding the same complete group again from another `x` index cannot discover a shorter path to any member; it would only repeat already considered edges.

Across the entire search, each value list is expanded at most once. This deletion is the key optimization that keeps a large repeated-value group from being scanned once per member.

Adjacent jumps guarantee that the target is always reachable, even if no useful equal-value jump exists. Therefore, the unconditional `while 1` loop will eventually pop the last index and return.

The BFS invariant establishes the answer: every queued node has been reached by a valid path, nodes are popped in nondecreasing jump count, and every outgoing edge of a popped node is considered either directly or during the one safe expansion of its value group. The first target pop is thus the minimum possible number of jumps.

## Complexity detail

Let $n$ be the array length.

Building `g` takes $O(n)$ expected time. Every index is inserted into one bucket. During BFS, each index enters the queue at most once because of `vis`. Its two adjacent candidates are checked once. Although a value bucket can contain many indices, `pop` ensures each bucket is expanded only once, so the total number of same-value entries expanded over all buckets is $n$.

The total expected time is therefore $O(n)$. Dictionary and set operations use expected $O(1)$ hash-table time.

The value-to-indices lists collectively store $n$ indices. The queue and visited set can each hold $O(n)$ indices. Expanding a bucket with the starred tuple can also create a temporary tuple proportional to that bucket’s size, but only one such tuple exists for the current node and its peak size is $O(n)$. Overall auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Bidirectional BFS:** Search simultaneously from index zero and the last index, expanding the smaller frontier. It has the same $O(n)$ worst-case bounds and can reduce practical work.
- **Repeated equal-value scans:** Looking through the full array for matches at every node is correct but can take $O(n^2)$ time.
- **Keeping buckets after expansion:** Even with a precomputed map, scanning the same large list from every matching node can become quadratic. Removing the bucket is essential.
- **Current index inside its own bucket:** It is harmless because `vis` already contains it, so it is never enqueued again.
- **One-element array:** The starting index is the target, so zero jumps are returned.
- **First and last values equal:** The last index is discovered from the first bucket expansion and returned at distance one.
- **All values equal:** Every index is enqueued from index zero in one expansion; the answer is one when $n > 1$.
- **All values distinct:** Equal-value buckets add no useful move, and BFS reduces to walking through adjacent indices.
- **Negative values:** Dictionary keys support them exactly like positive values; only equality matters.
- **Out-of-bounds adjacent index:** The range test rejects `-1` and `n` candidates safely.
- **Mark on enqueue:** Delaying the visited mark until dequeue would allow the same index to enter the queue several times from one layer.
