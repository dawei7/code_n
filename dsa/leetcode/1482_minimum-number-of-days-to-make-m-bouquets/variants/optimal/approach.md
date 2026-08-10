## General

**Turn a day into a monotone feasibility question.** `check(days)` asks whether at least `m` bouquets can be formed using flowers whose bloom day is at most `days`. If a day is feasible, every later day is also feasible because flowers never become unavailable.

This false-then-true pattern allows binary search for the first feasible day.

**Count disjoint adjacent groups.** `cur` counts consecutive bloomed, unused flowers. An unbloomed flower resets it to zero because adjacency is broken. Whenever `cur == k`, one bouquet is completed, `cnt` increases, and `cur` resets so those flowers cannot be reused.

Resetting after a bouquet is optimal: within a consecutive run of length `r`, exactly `floor(r/k)` disjoint bouquets can be made. Taking each group as soon as it reaches size `k` realizes that maximum.

The helper returns whether `cnt >= m`, not the exact count, because binary search needs only feasibility.

**Search through integer days with bisect.** `mx` is the latest bloom day. `range(mx + 2)` represents candidates zero through `mx+1`. `bisect_left` with `key=check` searches the monotone Boolean keys for the first value equal to true.

If production is possible, all flowers have bloomed by `mx`, so the first feasible day is at most `mx`. If even all flowers cannot provide enough disjoint groups, every key through `mx+1` is false and insertion position `l` exceeds `mx`; the method returns `-1`.

This cleverly incorporates the usual preliminary test `m*k > n` without writing it explicitly.
The scan counts the maximum bouquets possible by the candidate day because each maximal bloomed run contributes its maximum number of disjoint length-`k` groups. Feasibility is monotone in days. Binary search returns the smallest candidate whose check is true, which is exactly the minimum waiting time.

For `k=1` every bloomed flower immediately creates a bouquet. For larger `k`, an unbloomed position correctly separates runs even if many flowers have bloomed elsewhere.

**Why greedy grouping inside a run is safe.** Suppose a bloomed run contains `r` consecutive flowers. Any bouquet consumes `k` of them, so no method can form more than `floor(r/k)` bouquets from the run. Taking the first `k`, resetting, and repeating achieves exactly that bound. There is no benefit in shifting a bouquet inside the run because only the number of disjoint groups matters, not their positions.

Different runs cannot share a bouquet because an unbloomed flower lies between them. Summing the greedy count from each run is therefore the global maximum for that candidate day.

**Understand what bisect sees.** The search sequence is not a stored Boolean list. `range` supplies a candidate integer only when binary search probes it, and `key=check` computes that candidate's Boolean value on demand. Since Python orders `False` before `True`, asking for the left insertion position of `True` locates the first feasible candidate.

The extra candidate `mx + 1` acts as a sentinel probe beyond the meaningful maximum bloom day. If the instance is feasible, feasibility must begin no later than `mx`. A returned position above `mx` therefore proves impossibility without multiplying `m*k`, which also avoids any fixed-width overflow concern found in other languages.

**A separated-run example.** On day seven, availability pattern `true,true,true,true,false,true,true` with `k=3` yields one bouquet from the first run of length four and zero from the last run of length two. Five total bloomed flowers are not enough for two bouquets because adjacency, not only total count, controls feasibility.

## Complexity detail

Let `N` be flower count and `D = max(bloomDay)`. Each check scans `N` entries in `O(N)` time and constant space.

Binary search performs `O(log D)` checks over the integer range, giving `O(N log D)` time. Apart from helper counters and range/bisect state, auxiliary space is `O(1)`, matching the manifest.

The range object is lazy and does not allocate `D` integers.

## Alternatives and edge cases

- **Explicit binary-search loop:** Maintain low and high boundaries manually; it expresses the same monotone search without `bisect_left(key=...)`.
- **Precheck m times k:** Returning `-1` immediately when too few flowers exist can avoid all checks.
- **Scan every day:** It may require up to `D` full passes and is too slow.
- **k equals one:** Bouquet count equals number of bloomed flowers.
- **m times k exceeds N:** Even day `mx` is infeasible and the result is `-1`.
- **All bloom together:** The answer is that common day if enough flowers exist.
- **Adjacency broken:** An unavailable flower resets `cur`.
- **Long bloomed run:** Resetting at `k` extracts every disjoint bouquet.
- **Exact m bouquets:** Feasibility uses `>=` because extra possible bouquets do not hurt.
- **Day zero:** No positive bloom day is available, so it is normally false.
- **Maximum day:** All flowers are available and feasibility depends only on count.
- **Lazy range:** The enormous day domain is searched without materialization.
- **Duplicate bloom days:** Several flowers become available together, and monotonicity still holds.
- **Candidate between bloom events:** Feasibility matches the previous event day, but binary search may probe it safely.
- **No flower blooms by a candidate:** Every run length is zero and check returns false.
- **Reset after k:** It prevents one flower from participating in two bouquets.
