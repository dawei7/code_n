## General

**View reachable indices as breadth-first layers**

From index 0, one jump can reach an interval of indices. From every index in that interval, a second jump can reach a larger interval, and so on. Because jumps only move forward and each index permits every distance up to its maximum, the set reachable within a fixed number of jumps forms a continuous prefix rather than scattered positions.

This lets the algorithm perform the equivalent of breadth-first search without storing a queue. Each “layer” consists of indices reachable using the current number of jumps. Finishing a layer and extending to the next one corresponds to committing exactly one additional jump. The first layer whose range contains the final index therefore gives the minimum number of jumps, just as ordinary breadth-first search finds a shortest unweighted path.

**Meaning of the three variables**

`ans` is the number of jumps committed so far. `last` is the rightmost index reachable with those committed jumps; it is the boundary of the current layer. `mx` is the farthest index that could be reached with one more jump from any current-layer index scanned so far.

Initially all three are zero. With zero jumps, only index 0 is reachable, so `last = 0` is correct. No outgoing jump has yet been examined, so the best next reach is also initialized to zero.

At index `i`, the value `i + x` is the farthest destination of a jump starting there. The assignment `mx = max(mx, i + x)` preserves the best destination found across every starting point considered in the current layer. Choosing the locally longest jump from the first index would be unsafe; the farthest next reach must be compared across the entire current layer.

**Commit only at a layer boundary**

When `i == last`, the scan has now processed every index reachable with `ans` jumps. Before testing the boundary, it has already incorporated the outgoing reach `i + x`, so the boundary index's jump options are not omitted. The algorithm increments `ans` and sets `last = mx`.

This update means one more jump can reach every index up to the best boundary found from the completed layer. There is no reason to decide which exact predecessor index supplied `mx` because only the minimum count is requested, not the path itself.

For `[2, 3, 1, 1, 4]`, processing index 0 gives `mx = 2`. Since index 0 is the zero-jump boundary, the algorithm commits jump 1 and sets `last = 2`. It then examines indices 1 and 2, both reachable in one jump. Their best outgoing reach becomes 4. At boundary index 2 it commits jump 2 and sets `last = 4`, which includes the final index. No third jump is counted.

**Why the final index is deliberately excluded**

The loop iterates over `nums[:-1]`, so it processes indices 0 through $n-2$. Reaching index $n-1$ completes the task; its outgoing jump length is irrelevant. If the last index were processed and happened to equal a layer boundary, the code could count a jump *from* the destination after already arriving there.

Stopping before the final index also makes the single-element case natural. When $n=1$, the slice is empty, the loop performs no work, and `ans = 0` is returned because the starting index is already the destination.

**The invariant that proves minimality**

Immediately after a boundary update, `last` is the farthest index reachable using exactly `ans` jumps, or equivalently within at most `ans` jumps because all earlier positions lie in the same prefix. While scanning indices through that boundary, `mx` becomes the farthest point reachable with one additional jump.

No index beyond `mx` can be reached in `ans + 1` jumps: every possible penultimate index lies at or before `last`, all of those indices are scanned, and `mx` is the maximum of their farthest destinations. Conversely, the index achieving `mx` is reachable within `ans` jumps and has a legal jump to `mx`, so that bound is attainable.

Thus each update computes the exact next breadth-first boundary. Since `ans` increases only after exhausting all possibilities using fewer jumps, it cannot overstate the minimum. The reachability guarantee ensures each necessary boundary advances and the scan never becomes trapped before the destination.

**A Python slicing caveat**

Algorithmically, this greedy scan needs only constant scalar state. However, the exact expression `nums[:-1]` creates a new list containing $n-1$ elements in Python. That allocation makes the selected source's actual auxiliary-space usage $O(n)$, contrary to the manifest's $O(1)$ claim.

Using `for i in range(n - 1)` and reading `nums[i]` would preserve the same greedy logic while genuinely using $O(1)$ auxiliary space. The protected source is not changed here; the explanation distinguishes the conceptual method from the concrete cost of its slice.

## Complexity detail

The loop examines each index before the destination once, and each iteration performs constant-time arithmetic and comparisons. Constructing `nums[:-1]` also copies $n-1$ references once. Total time remains $O(n)$.

The greedy variables themselves use $O(1)$ space, but the Python slice occupies $O(n)$ additional memory. Therefore, the exact selected implementation uses $O(n)$ auxiliary space, not the $O(1)$ listed in the manifest. Replacing the slice with index-based iteration would make the manifest bound accurate without changing the algorithm.

## Alternatives and edge cases

- **Index-based greedy loop:** Iterate `range(len(nums) - 1)` to avoid the slice. This is the direct way to retain $O(n)$ time and achieve true $O(1)$ auxiliary space.
- **Explicit breadth-first search:** Enqueue every reachable index by levels. It makes shortest-path reasoning familiar but can revisit ranges or require $O(n)$ queue/visited storage unless carefully optimized.
- **Dynamic programming:** Let each position store the fewest jumps needed to reach it. A straightforward transition from every earlier position costs $O(n^2)$ time and $O(n)$ space.
- **Choose the largest immediate jump:** Selecting the largest `nums[i]` rather than the farthest `i + nums[i]` from the entire layer can be suboptimal. The layer maximum compares all reachable launch points.
- **One-element input:** No jump is needed; excluding the last index leaves `ans` at zero.
- **Zeros inside the array:** A zero contributes no extension, but other indices in the same reachable layer may extend `mx`. Reachability guarantees the whole layer will not stall before the end.
- **Destination reached before scanning ends:** Once the boundary includes the final index, no later boundary at or before $n-2$ is needed, so no extra jump is counted.
- **Unreachable input outside the contract:** This source has no explicit failure detection. Its correctness and boundary progress rely on the guarantee that the last index is reachable.
- **Input preservation:** Apart from allocating a slice, the method only reads values and does not mutate `nums`.
