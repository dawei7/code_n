## General

**Compress breadth-first search into interval boundaries**

Treat each array index as a node and every legal jump as an unweighted directed edge to a later index. The minimum jump count is a shortest-path distance, which suggests breadth-first search. Listing all edges or storing a queue would be wasteful, but forward jumps have interval structure: if an index can jump length `k`, it can reach every next index through `i + k`.

The selected solution represents a breadth-first layer only by its farthest boundary. `curr_reachable` is the farthest index reachable with the currently counted number of jumps. `reachable` is the farthest index discovered by taking one more jump from positions scanned so far. `jump_count` identifies the current layer's distance.

**Initialization at the start position**

All three numeric variables begin at zero. With zero jumps, index 0 is the only reachable position, so `curr_reachable = 0` is the correct current boundary. Before processing index 0's outgoing jump, the best known reach is also zero. For a one-element list, the scan never needs to enter a later layer, so the returned count remains zero.

**Why the boundary test happens before extending from `i`**

At each index, the source first checks `i > reachable`. If true, even the best jump from every previously scanned reachable index falls short of `i`. The position cannot be visited, and because all later indices are farther right, the destination is unreachable. The method returns `-1`. Official inputs guarantee reachability, so this branch should not execute there, but it makes the source robust to a stalled frontier.

Next, if `i > curr_reachable`, the scan has moved beyond the old breadth-first layer. Reaching index `i` requires entering the next layer, so the code increments `jump_count` and promotes the previously accumulated `reachable` boundary into `curr_reachable`.

Only then does it evaluate `i + length` and extend `reachable`. That new jump belongs to the newly entered current layer and is a candidate boundary for the following layer, not evidence that `i` was reachable with fewer jumps. Keeping this order preserves the distance meaning of the two frontiers.

**A step-by-step example**

For `[2, 3, 1, 1, 4]`, index 0 extends `reachable` to 2 without increasing the count. At index 1, `i > curr_reachable` is true because the zero-jump layer ended at 0. The algorithm promotes boundary 2 and sets `jump_count = 1`. Processing indices 1 and 2 extends `reachable` as far as 4.

At index 3, the scan crosses boundary 2. It promotes 4 and increments the count to 2. The final index 4 is inside that boundary, so no third increment occurs. The method returns 2.

Unlike the other branch's loop, this implementation scans the final array element too. That remains correct because a jump is counted only when entering an index beyond the previous boundary, not merely because an index is processed. Entering the last index may legitimately be the moment the final jump count is recognized; its outgoing reach is calculated afterward but cannot cause another count because the loop ends.

**Why taking the farthest frontier is optimal**

Suppose all indices through `curr_reachable` are reachable within `jump_count` jumps. The scan processes every one of them before crossing that boundary and sets `reachable` to the maximum of `i + A[i]`. Therefore, every index at or before `reachable` can be reached with at most one additional jump.

No index beyond `reachable` can be reached in that many jumps, because any final jump would have to begin at an index in the just-processed layer, and the maximum endpoint over all such starts is exactly `reachable`. Promoting it therefore constructs the exact next BFS boundary.

Because `jump_count` increases only when the scan leaves a fully processed boundary, all possibilities using fewer jumps have already been exhausted. This is why a greedy maximum produces the global minimum rather than merely a locally attractive path.

**`reachable` versus `curr_reachable`**

The names are similar but cannot be merged. `curr_reachable` answers “how far can the current number of jumps take us?” `reachable` answers “how far could one more jump take us based on everything scanned?” Updating the current boundary on every index would blur layer transitions and could count incorrectly. Delaying promotion until `i` crosses the old boundary is what turns reachability into a minimum jump count.

## Complexity detail

`enumerate(A)` visits each of the $n$ positions once. Pointer comparisons, maximum updates, and counter changes are constant-time operations, so total time is $O(n)$.

Only three integer state variables plus the loop pair are stored. No array slice, queue, dynamic-programming table, or recursion stack is created. Auxiliary space is genuinely $O(1)$, matching the manifest. The input list is read without mutation.

## Alternatives and edge cases

- **Boundary update at `i == current_end`:** Scan only through index $n-2$, accumulate the next farthest reach, and count a jump when finishing the current layer. This is an equivalent greedy schedule.
- **Explicit queue BFS:** It guarantees shortest paths but storing indices and generating every outgoing edge can cost much more time and space than exploiting interval reachability.
- **Quadratic dynamic programming:** Compute the best jump count for every destination from all prior reachable indices. It is conceptually direct but costs $O(n^2)$ time.
- **Track the actual path:** Store which index achieved each frontier if the jump sequence itself is required. The problem asks only for the count, so predecessor storage is unnecessary.
- **One-element input:** No boundary crossing occurs, and zero jumps are returned.
- **A zero-length jump:** It does not extend `reachable`. Another index in the same layer may still advance the frontier.
- **Unreachable array:** If the scan reaches `i > reachable`, the source returns `-1`. This is outside the guaranteed test domain but is a meaningful failure signal.
- **Final index enters a new layer:** The `i > curr_reachable` check increments once upon entering it, which counts the last required jump. Its own jump length does not add another jump.
- **Very large jump:** `reachable` may exceed the final index. That is harmless; the method needs only to know the destination lies inside the frontier.
- **Input unchanged:** The solution does not sort, slice, or write to `A`.
