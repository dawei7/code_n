## General
**Reachable indices form a prefix summarized by one frontier**

Scan from left to right while tracking `farthest`, the greatest index reachable using positions already processed. Since a jump may use any distance up to its maximum, reachability through `farthest` is a contiguous prefix rather than a sparse set.

If the current index exceeds this frontier, it is unreachable, so its jump length cannot be used and no earlier position can cross the gap. Otherwise extend the frontier with `index + nums[index]`. Return early once it reaches the final index.

**Only reachable positions may extend the frontier**

Before processing index `i`, every position through `min(farthest, i - 1)` that matters to the scan is reachable, and `farthest` is the maximum endpoint of a jump from any reachable processed index. Thus `i <= farthest` is exactly the condition that permits using `nums[i]`.

**Trace a stalled frontier**

For `[3,2,1,0,4]`, index 0 sets the frontier to 3. Indices 1 through 3 cannot move it farther. Index 4 lies beyond the frontier, proving the zero at index 3 forms an uncrossable barrier.

**The frontier is the complete reachable prefix**

Every frontier extension is computed from an index already within the reachable prefix, so the jump witnessing that extension is legal. Because a jump may stop at any shorter distance, all positions up to the new maximum are reachable as well.

Conversely, no path leaving the processed prefix can land beyond the maximum endpoint contributed by its reachable indices. Encountering an index past the frontier therefore proves no legal path can cross the gap. If the frontier reaches the final index, the chain of jumps that created its successive extensions witnesses a valid route.

## Complexity detail
Each index is inspected at most once, so time is $O(n)$. The frontier and loop index use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Reachability dynamic programming:** records every reachable index and may test or mark $O(n^2)$ transitions.
- **Breadth-first search over jumps:** models the graph directly but materializes many redundant edges and states.
- **Work backward from the goal:** greedily moving the required goal leftward also yields $O(n)$ time and $O(1)$ space.
- A one-element array is already at the destination, even when its only jump length is zero.
- Large jump lengths may pass beyond the array; reaching at least the final index is sufficient because a shorter legal landing can be chosen.
