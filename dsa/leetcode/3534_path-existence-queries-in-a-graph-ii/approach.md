## General

**Sort nodes by value while preserving their identities**

Edges depend only on value differences, not original array positions. The source creates:

`pairs = sorted((value, original_index) for original_index, value in enumerate(nums))`.

Sorted position gives left-to-right value order, while the stored original index lets query nodes and jump-table entries retain their identities.

Equal values are ordered by original index as Python compares tuple second fields, but every pair of equal-valued nodes has difference zero and is directly connected. Their internal sorted order does not change distances to different value levels.

**Define the farthest useful one-edge jump**

For a node of value `v`, every node whose value lies between `v` and `v + maxDiff` is reachable in one edge. Among those, moving to the largest value gives the greatest progress toward any target to the right.

The source defines `f[node][0]` as the original index of that farthest reachable node in sorted order.

It computes these values with a reverse two-pointer scan. `l` moves from the largest sorted position toward zero. Pointer `r` starts at the last position and moves left while:

`pairs[r].value - pairs[l].value > maxDiff`.

When the loop stops, `r` is the farthest sorted position whose value is within one edge of `l`. As `l` moves left, its allowed upper value does not increase, so `r` never needs to move right again. Total pointer movement is linear.

`r` can never pass `l` because a node differs from itself by zero, which is always at most the nonnegative threshold.

**Why always jumping farthest is optimal**

Consider traveling from a smaller value toward a larger target. From current value `v`, any legal next value is at most the farthest reachable value `F(v)`.

Starting from a farther-right value cannot reduce the farthest value reachable on the next step: its allowed interval ends at that value plus `maxDiff`, and the sorted available nodes up to that boundary include progress at least as far as any smaller choice can enable.

By induction, after `t` edges, repeated farthest jumps reach a value at least as large as the endpoint of any other `t`-edge path that moves toward the target. Backward movement cannot improve rightward reach because it only lowers the next interval's upper boundary.

Therefore, the minimum path length to a higher target is the smallest number of repeated farthest jumps needed to reach a value at least as large as the target. If the farthest map stops below the target, the nodes lie in different components.

**Build a binary-lifting table**

`f[node][k]` stores the node reached after `2^k` repeated farthest jumps.

The recurrence is:

`f[node][k] = f[f[node][k-1]][k-1]`.

The source uses exactly 20 levels. The largest relevant simple shortest path has fewer than `n <= 100,000` edges, and `2^17 > 100,000`, so 20 levels are more than sufficient.

The table is filled while `l` moves from right to left. A node's one-step destination is at the same or a later sorted position. Later positions have already been processed in this reverse scan, so their higher jump entries are ready when the recurrence reads them. A node that maps to itself also builds a stable self-loop at every level.

**Orient each query by value**

For query original indices `i,j`, if `nums[i] > nums[j]`, the source swaps them. The remaining logic always moves from the lower value toward the higher value.

If `i == j`, the distance is zero: no edge is needed.

If the indices differ but their values are equal, their absolute difference is zero, so a direct edge exists and the distance is one. The source handles this before binary lifting. This distinction between same node and same value is essential.

**Use lifting to find how many jumps remain strictly below the target**

Let the target value be `nums[j]`. Starting with `d = 0`, the source scans powers from largest to smallest. If:

`nums[f[i][k]] < nums[j]`,

then even after `2^k` greedy jumps the current value remains strictly below the target. Those jumps are safe to take without reaching or passing it, so the source:

- moves `i = f[i][k]`;
- records that jump count with `d |= 1 << k`.

Bitwise OR is equivalent to addition here because each power of two is considered at most once and the corresponding bit in `d` was previously zero.

After the descending scan, `d` is the largest number of greedy jumps known to remain below the target.

**Decide reachability and add the final edge**

If `nums[f[i][0]] < nums[j]` still holds, one more farthest jump cannot reach the target value. At this point the farthest map has become stuck at the rightmost node of a lower connected component, so the target is unreachable and the source returns `-1`.

Otherwise, the target value lies no farther right than the farthest one-edge destination. Since every intermediate value within `maxDiff` is directly adjacent to current `i`, the actual target node can be reached in one final edge. The answer is `d + 1`.

The jump may “pass” the target in sorted order, but the algorithm does not need to land on the farthest node. Its existence certifies that the target itself is within the same one-edge value interval.

**Why binary lifting returns the shortest distance**

Repeated farthest jumps dominate every path with the same number of edges. The lifting loop finds the largest `d` for which greedy progress is still below the target. Thus no path of `d` edges can reach it. If the final one-edge test succeeds, a path of `d+1` edges exists. These matching lower and upper bounds prove the returned distance is minimum.

If the test fails, even unlimited greedy jumps remain trapped below a value gap larger than `maxDiff`; no alternative shorter jump can cross a boundary that the farthest option cannot cross.

## Complexity detail

Sorting `n` value-index pairs costs `O(n log n)`. The reverse pointer `r` moves at most `n-1` times total. Filling 20 jump entries for each node costs `O(n log n)` with the fixed level count corresponding to `O(log n)`.

Each of `Q` queries scans 20 levels, taking `O(log n)` time. Total time is `O((n+Q) log n)`.

The jump table contains `20n = O(n log n)` integer references. The sorted pairs and output use `O(n)` and `O(Q)` respectively. Auxiliary preprocessing space matches the manifest's `O(n log n)`.

The fixed constant 20 is correct only because of the stated `n <= 100,000`. A general implementation should use `n.bit_length()` so the level count adapts automatically.

## Alternatives and edge cases

- **Breadth-first search per query:** The implicit graph may be dense and `Q` may be `100,000`, making repeated traversal far too expensive.
- **Build all edges:** Up to `O(n^2)` node pairs may satisfy the threshold. Sorted intervals describe reach without materializing them.
- **Repeated one-step greedy jumps:** Correct, but a query can require `O(n)` jumps. Binary lifting composes them in logarithmic time.
- **Use original index order:** Edge structure depends on values, so sorting by value is essential.
- **Jump to any reachable node rather than the farthest:** It remains a valid path but may use more edges. Farthest progress gives the shortest-hop frontier.
- **Same original node:** Distance is zero even though the graph may contain self-independent edges.
- **Different nodes with equal values:** Their difference is zero and their distance is one; the explicit equality case handles them.
- **maxDiff equals zero:** Only equal-valued distinct nodes are connected. Farthest jumps stay within one equal-value group.
- **Target directly reachable:** No lifting jump remains strictly below it, so `d=0` and the answer is one.
- **Disconnected components:** The farthest map stabilizes below the target and the final test returns `-1`.
- **Duplicate values at the farthest boundary:** Any duplicate node at that value provides equivalent future reach; tuple ordering chooses one deterministically.
- **Going backward in value:** It cannot improve a rightward shortest path because it reduces the next maximum reachable value.
- **Fixed table height:** Twenty levels cover the current constraints but should not be copied blindly to a larger-`n` version.
- **Undirected edges:** Orienting the query by value is an analysis convenience; every step used remains a valid undirected edge.
