## General

**Reduce clips with the same start to one useful reach**

To cover `[0, time]` continuously, the first selected clip must begin at zero, and every later selected clip must begin no later than the point already covered. Overlap is allowed because clips may be cut freely. Therefore, when several clips have the same starting time, only the one ending farthest to the right can matter. A shorter clip with that start never reaches a point the longer clip cannot reach, and both cost one selection.

The array `last` records this compressed information. It has one entry for every integer start from zero through `time - 1`. For a clip `[a, b]` with `a < time`, the assignment `last[a] = max(last[a], b)` keeps the farthest endpoint among clips starting exactly at `a`.

A clip starting at or after `time` cannot help cover any missing point before `time`, so the code ignores it. The source constraints use integer endpoints, which is why an array indexed by start time can replace sorting.

**The three greedy variables**

During the scan, `i` is the current time position, `mx` is the farthest endpoint among every clip whose start is at most `i`, and `pre` is the endpoint guaranteed by the clips already counted in `ans`.

At each index, `mx = max(mx, v)` incorporates the best clip starting at that exact `i`. Because `mx` never decreases, after this update it is the farthest reach of any clip seen from starts zero through `i`.

The variable `pre` acts like the end of the current greedy layer. As long as `i < pre`, the clips already counted cover the present position, so the method keeps scanning starts and improving `mx`. When `i == pre`, the current selection can take coverage no farther. To continue, one more clip must be committed. The algorithm increments `ans` and sets `pre = mx`, conceptually choosing the available clip that reaches farthest.

The code does not need to remember that clip's identity because the answer asks only for the minimum count. The farthest endpoint contains all information needed for the next layer.

**Why choosing the farthest reach is optimal**

Suppose the existing selections cover through time `pre`. Any legal next clip must start at or before `pre`; otherwise, there would be an uncovered gap immediately after `pre`. Among all such clips, let the greedy choice end at `mx`.

Consider any optimal solution and its next clip at the same point. That clip ends no later than `mx` because `mx` is the maximum endpoint among all legal candidates. Replace the optimal solution's next clip with the greedy clip. The replacement still overlaps the covered prefix, uses the same one-clip cost, and covers at least as far. It cannot make the remainder harder to cover.

Applying this exchange at every boundary shows that there is an optimal solution agreeing with each greedy extension. Therefore, counting one clip whenever the current layer ends yields the minimum possible number.

Another useful interpretation is the minimum-jumps pattern. All starts reachable with `ans` clips are scanned, `mx` records the farthest point reachable with one additional clip, and reaching `pre` closes the current layer.

**Why the impossibility check comes first**

After incorporating `last[i]`, the condition `if mx <= i: return -1` asks whether any clip starting no later than `i` extends strictly beyond `i`.

If not, coverage cannot cross that position. A clip starting later than `i` leaves a gap, while every clip starting at or before `i` ends at or before `i`. Cutting clips cannot create footage outside their original intervals, so no solution exists.

The strict inequality matters. An endpoint equal to `i` reaches the point `i` but does not cover any interval immediately after it. To continue toward a larger target, reach must be greater than `i`.

This test is evaluated before a possible `pre == i` selection. It prevents the algorithm from incrementing the answer for a nonexistent extension.

**Trace the first example**

For `time = 10`, the useful starts include reach two from start zero, reach nine from start one, and reach ten from start eight.

At `i = 0`, `mx` becomes two. It is greater than zero, and `pre` is zero, so the algorithm selects its first clip, sets `ans = 1`, and moves `pre` to two.

At `i = 1`, the clip ending at nine becomes available, so `mx` becomes nine. The scan does not select it immediately because `i` has not yet reached `pre`. At `i = 2`, the current layer ends. The farthest candidate seen so far reaches nine, so the second selection changes `pre` to nine.

The scan continues through starts below nine. At `i = 8`, the clip ending at ten becomes available and updates `mx`. At `i = 9`, the second layer ends, so the third selection moves `pre` to ten. The loop only visits indices zero through nine; reaching ten means the whole target is covered, and the method returns three.

Notice that the last clip may start at eight even though the preceding guaranteed boundary is nine. Overlap is legal, and starting before the boundary is exactly what prevents a gap.

**Why scanning every integer start is sufficient**

All clip endpoints and `time` are integers under the contract. Coverage changes only when a clip start becomes available or when a selected reach ends, both of which occur at integer values. The array scan therefore sees every relevant event.

At an index smaller than `pre`, the algorithm merely gathers options. At exactly `pre`, it commits the best gathered option. If `pre` jumps to or beyond `time`, no further commitment is needed. Because `enumerate(last)` stops at `time - 1`, the method returns immediately after enough clips have been counted to cover the target.

**Why the returned count is correct**

The invariant is that `ans` clips can cover continuously from zero through `pre`, while `mx` is the farthest reach obtainable by adding one clip whose start has already been scanned. The preprocessing guarantees that no useful endpoint for a scanned start was discarded.

At a layer boundary, the farthest-reach exchange proves that extending to `mx` is compatible with an optimal solution. If reach cannot pass the current index, the gap proof establishes impossibility. If the scan completes, the last committed boundary reaches at least `time`. Thus the returned value is both feasible and no larger than the clip count of any other feasible construction.

## Complexity detail

Let `N` be the number of clips and `T = time`. Building `last` examines every clip once, taking `O(N)` time. Scanning the `T` array entries takes `O(T)` time. Every operation inside either loop is constant time, so total time is `O(N + T)`, matching the manifest.

The `last` array contains `T` integers and uses `O(T)` space. The variables `ans`, `mx`, `pre`, and loop values require constant additional storage. No sorting or reconstruction list is created, so the total auxiliary bound is `O(T)`.

## Alternatives and edge cases

- **Sort clips by starting time:** Scan sorted intervals and repeatedly choose the farthest endpoint among clips starting before the current boundary. This is the general interval-cover greedy and uses `O(N \log N)` time; the bounded integer timeline lets the exact solution avoid sorting.
- **Dynamic programming over time:** Let a state store the minimum clips needed to cover each endpoint and relax with every interval. It can be correct, but it obscures the farthest-reach exchange and usually costs more than `O(N + T)`.
- **Breadth-first reach layers:** Treat each newly reachable endpoint as a layer. This mirrors the greedy jump interpretation but needs extra state unless compressed to the same `pre` and `mx` variables.
- **Several clips with one start:** Only the maximum end is retained. Every shorter one has the same cost and no coverage advantage.
- **Zero-length clips:** A clip `[a, a]` cannot extend coverage. It may be stored, but `mx <= i` prevents it from creating false progress.
- **No clip beginning at zero:** At `i = 0`, `mx` remains zero, so the method immediately returns `-1`.
- **A clip covering the whole event:** If `[0, b]` has `b >= time`, the first commitment sets `pre` beyond the target and the final answer is one.
- **Endpoint touching:** A clip ending at `x` and another starting at `x` connect without a gap because the intervals include that boundary and clips may be cut.
- **Clip starting beyond the target:** It is ignored because it cannot contribute to covering any point before `time`.
- **Reach beyond `time`:** Endpoints are not clamped. A reach larger than the target is harmless and correctly signifies completion.
- **Duplicate boundary choices:** The method counts only when `pre == i`. Since `pre` strictly advances on every successful commitment, the same boundary cannot be counted twice.
- **Impossible late gap:** Even if an initial prefix is covered, the method returns `-1` at the first index that no available interval can cross.
