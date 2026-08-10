## General

**Track the farthest landing discovered so far**

`reachable` begins at 0 because the player starts at index 0. While scanning the array from left to right, every index `i` at or below this frontier can be visited. Its maximum jump extends to `i + length`, so the frontier becomes the larger of its old value and that destination.

This one number summarizes all earlier path choices. It is valid because a maximum jump of `k` permits every shorter jump. If a reachable launch point covers an interval ending at some destination, every position in that interval is reachable, and unions of these overlapping forward intervals remain a prefix.

**Break when the scan reaches an unreachable index**

Before using `A[i]`, the code checks `i > reachable`. If true, all previously processed reachable indices fall short of `i`. Since later positions are even farther right and jumps never move backward into a launch position, no later value can repair the gap. The loop breaks.

The code does not immediately return false because it uses one common final expression. After a break, `reachable` is still below `i`, and therefore below the final index unless the final index had already been reached. The final comparison produces the correct result.

If `i` is reachable, `reachable = max(reachable, i + length)` incorporates its outgoing interval. An unreachable index is never allowed to extend the frontier because the gap check comes first.

**A precise invariant**

At the start of every normal iteration, all indices from 0 through `reachable` are known reachable, and no farther endpoint has been discovered from processed positions. When `i <= reachable`, the current position belongs to that prefix. Every landing from `i` through `i + A[i]` is legal, so taking the maximum gives the new exact discovered frontier.

When `i > reachable`, all possible positions capable of reaching `i` are earlier than it and have already been processed. None reached far enough, proving the gap permanent.

**Why the final comparison is sufficient**

After the loop ends—either normally or through `break`—the destination is reachable exactly when `reachable >= len(A) - 1`. The frontier may extend beyond the physical array; only comparison with the final valid index matters.

If the loop completes normally, every scanned position was reachable, including the last one. If it breaks early, the last index can be reachable only if it was already inside a frontier that overshot the gap, but then the current `i` would also be inside that frontier and the break would not have occurred. The comparison handles both cases consistently.

**Successful and failed examples**

For `[2,3,1,1,4]`, index 0 sets the frontier to 2, and index 1 extends it to 4. The final comparison is true. For `[3,2,1,0,4]`, the frontier reaches only 3. The scan breaks at index 4 and returns false.

A zero is not automatically fatal. It matters only when every reachable launch point fails to extend beyond it. Likewise, a very large value beyond an unreachable gap is useless because the algorithm correctly refuses to process it.

**Relation to minimum-jump counting**

This problem asks only whether the final index belongs to the reachable prefix. It does not need the separate current-layer and next-layer boundaries used to find a minimum jump count. One farthest frontier is enough for a Boolean answer.

The method also does not commit to a particular landing at each step. A frontier may be supplied by one index while an interior position supplies the next extension. Retaining the whole reachable prefix, rather than one imagined path, is precisely why a locally computed maximum remains globally complete.

## Complexity detail

`enumerate(A)` processes at most $n$ values, stopping early if it encounters a gap. Each iteration uses constant-time work, so time is $O(n)$.

The algorithm stores one frontier plus loop variables and allocates no size-dependent structure. Auxiliary space is $O(1)$, matching the manifest. It does not mutate the input.

## Alternatives and edge cases

- **Immediate false return:** Return as soon as `i > reachable` instead of breaking. This is behaviorally equivalent to the final comparison for this traversal.
- **Early success return:** Stop once the frontier covers the last index. It can save iterations on easy inputs but does not improve the worst-case bound.
- **Backward target scan:** Move a goal index left whenever a position reaches it. Success means index 0 becomes the goal.
- **Memoized recursion:** Explore landing choices and cache failed indices. It uses $O(n)$ memory and can still inspect many edges that interval greediness avoids.
- **Single-element array:** `reachable` already equals the destination index, so true is returned.
- **Reachable zero:** Other positions may have extended the frontier beyond it, allowing the scan to continue.
- **Unreachable positive value:** It cannot contribute because the gap check occurs before the update.
- **Overshoot:** A frontier beyond `len(A) - 1` is valid evidence of reaching the destination.
- **Exact-jump variant:** If only the full listed distance were permitted, reachable positions might not form a prefix and this greedy proof would fail.
- **Input unchanged:** The method reads but never writes or slices `A`.
