## General

**Binary-search the answer rather than the placements**

For a proposed minimum force `f`, ask a yes-or-no question: can at least `m` balls be placed so every consecutive chosen position is separated by at least `f`?

If a force is feasible, every smaller force is feasible using the same placement. If a force is infeasible, every larger force is also infeasible because it only tightens the spacing requirement.

This monotone transition from feasible to infeasible permits binary search over force values.

The positions must first be sorted. In sorted order, the minimum distance between any pair of selected balls is attained by some consecutive pair in the selected order. Ensuring every consecutive selected gap is at least `f` therefore ensures every pairwise distance is at least `f`.

**Greedily test one candidate force**

Helper `check(f)` scans sorted basket positions and greedily places each next ball in the earliest basket far enough from the last selected basket.

`prev` starts at negative infinity, so the first position always satisfies `curr - prev >= f`. The source counts it and records it as the most recent placement.

For each later `curr`, it places a ball when `curr - prev >= f`, then updates `prev` and increments `cnt`. Positions that are too close are skipped.

The helper finally returns `cnt < m`. This return value means “infeasible,” which is the reverse of many feasibility helpers: `False` means enough balls fit, while `True` means they do not.

**Why earliest feasible placement maximizes the count**

Suppose the previous ball is fixed. Among all baskets that are at least `f` away, choosing the leftmost one leaves at least as much space for every later ball as choosing a farther-right basket.

If some feasible arrangement chooses a later basket at this step, replace it with the greedy earlier basket. The replacement still respects the previous gap and cannot invalidate any later gap because it only moves the current ball left.

Repeating this exchange shows that if any placement of `m` balls exists for `f`, the greedy scan places at least `m`. Therefore `check` classifies feasibility exactly.

**Understand the virtual range and bisect result**

The source searches `range(l, r + 1)` with `l = 1` and `r = position[-1]`. A Python `range` is lazy, so it represents up to a billion force values without allocating them.

`bisect_left(..., True, key=check)` applies `check` to conceptual range elements and finds the first key equal to `True`, meaning the first infeasible force.

Importantly, `bisect_left` returns an insertion index, not the force value stored at that index. Because the range starts at one, index zero represents force one, index one represents force two, and so on.

If forces one through $D$ are feasible and $D+1$ is the first infeasible force, the first `True` occurs at zero-based index $D$. The returned insertion index is therefore exactly the maximum feasible force $D$.

This offset is deliberate. If the range started at zero, returning the raw index would need a different interpretation.

**Why an infeasible value exists in the range**

There are at least two balls, and basket positions are positive and distinct. A force equal to the maximum coordinate `position[-1]` cannot fit two balls: even the distance from the smallest positive coordinate to the maximum is strictly smaller.

Thus the key sequence contains a `True` before its end. Even if it did not, `bisect_left` would return the range length, but the problem constraints make the intended boundary explicit.

**Tracing the first example**

After sorting, positions are one, two, three, four, and seven.

For `f = 3`, greedy placement chooses one, then four, then seven. Three balls fit, so `check(3)` is false.

For `f = 4`, it chooses one, skips two through four, and chooses seven. Only two balls fit, so `check(4)` is true.

The first infeasible force is four, located at range index three. `bisect_left` returns three, the desired maximum feasible force.

**Why the returned force is optimal**

The greedy checker is exact, and its infeasibility predicate is monotone: false for all feasible forces followed by true for all infeasible forces.

Binary search locates the first infeasible force. The range-index offset converts that boundary to the preceding feasible force. Therefore the returned integer is both achievable and larger than every other achievable minimum distance.

## Complexity detail

Let $N$ be basket count and let $R$ be the searched coordinate range. Sorting costs $O(N\log N)$. Each `check` call scans all $N$ positions, and binary search makes $O(\log R)$ calls. Total time is $O(N\log N+N\log R)$, matching the manifest.

Python's in-place Timsort may use $O(N)$ temporary memory in the worst case, which matches the manifest's $O(N)$ space. The checker itself uses $O(1)$ state, and the virtual `range` occupies constant space regardless of its numeric length.

The exact source sorts `position` in place, so the caller-visible list order is changed.

## Alternatives and edge cases

- **Try every force linearly:** It can require up to a billion feasibility checks.
- **Enumerate ball combinations:** The number of placements is combinatorial.
- **Binary search with explicit bounds:** A conventional loop storing the largest feasible midpoint is equivalent and may be easier to recognize.
- **Unsorted positions:** Greedy earliest placement is defined only after sorting.
- **Two balls:** The optimum is the distance between the extreme basket positions.
- **m equals basket count:** Every basket is used, so the answer is the smallest adjacent sorted gap.
- **Huge coordinate gap:** The virtual `range` avoids allocating all candidate distances.
- **False-then-true key order:** `check` returns infeasibility specifically so the keys are ordered for `bisect_left`.
- **No early checker return:** The exact helper scans every position even after count reaches `m`; early success could improve constants.
- **Negative-infinity sentinel:** It guarantees selection of the first sorted basket without a special branch.
- **Distinct positions:** They guarantee a positive minimum force is possible.
- **Input mutation:** `position.sort()` permanently changes the supplied list's ordering.
- **Bisect key support:** The implementation relies on a Python version whose `bisect_left` accepts `key`.
