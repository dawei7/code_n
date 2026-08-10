## General

**Use prefix sums to recognize a target-sum subarray.** Let `s` be the sum of elements processed through current one-based position `i`. If an earlier prefix at position `j` has sum `s - target`, then elements from positions `j + 1` through `i` sum to target. Their length is `i - j`.

Dictionary `d` maps prefix sums to positions. It begins with `0: 0` so a target-sum subarray starting at the first element can use the empty prefix.

All array values are positive, so prefix sums strictly increase and each appears once. The assignment `d[s] = i` is therefore unambiguous.

**Store the best single subarray available to the left.** `f[i]` is the minimum length of any target-sum subarray ending at or before one-based position `i`. It starts as infinity everywhere.

At each position, `f[i] = f[i-1]` carries forward the best earlier subarray. If a new target interval `j+1..i` exists, `f[i]` also considers its length `i-j`.

This prefix-best array is the key to enforcing non-overlap without trying every pair.

**Combine the current interval with a completed left interval.** The current interval begins after prefix position `j`. Any subarray summarized by `f[j]` ends at or before `j`, so it cannot overlap the current interval.

The candidate total is `f[j] + i - j`. Updating `ans` with this value tries the best compatible left interval for every target interval ending at `i`.

Using `f[i]` instead would be unsafe because it may include the current interval itself or another interval extending beyond `j`. The boundary `j` is exactly what proves separation.

**Trace a simple example.** For `[7,3,4,7]` with target seven, position one finds interval `[7]` of length one and sets `f[1] = 1`, but no earlier interval exists to pair. Position three finds `[3,4]` beginning after position one, so it can combine with `f[1]` for total three. Position four finds another length-one `[7]` beginning after position three and combines with the best prefix interval of length one, producing answer two.

**Why every optimal pair is considered.** Order any two non-overlapping target intervals so the left one comes first. When the scan reaches the right interval's endpoint, prefix lookup discovers its start boundary `j`. The left interval ends by `j` and is represented in `f[j]`; that value is no longer than the chosen left interval. The algorithm therefore considers a pair at least as good.

Every candidate produced uses one real current target interval and one real prefix interval ending before it, so all candidates are valid. Taking the minimum yields the optimum.

**Separate the two kinds of minimum.** `f[i]` answers a reusable prefix question: what is the shortest single qualifying interval available so far? `ans` answers the final two-interval question. Updating `f` does not require a partner, while updating `ans` does. Keeping these roles separate prevents a newly found interval from being counted twice and lets the best old interval help many later candidates.

The one-based prefix positions also simplify length arithmetic. Prefix position `j` lies immediately before the current interval, so its length is `i - j` without an extra plus or minus one. The same boundary proves that an interval ending at `j` and one beginning at `j + 1` are adjacent but disjoint.

**Detect impossibility.** `ans` stays infinity unless two compatible intervals are found. Any real total length is at most `n`, so `ans > n` safely indicates absence and returns `-1`.

## Complexity detail

The scan visits each of `N` elements once. Prefix-map lookup and insertion are expected `O(1)`, and all DP updates are constant time. Expected time is `O(N)`.

The dictionary can hold `N + 1` prefix sums and `f` holds `N + 1` values, giving `O(N)` auxiliary space, matching the manifest.

Because values are positive, a sliding-window variant can achieve constant auxiliary space with carefully maintained best lengths, but the stored prefix approach uses linear memory.

Python infinity is a safe unreachable sentinel: adding a finite length leaves it infinite, so nonexistent left intervals cannot improve `ans`.

## Alternatives and edge cases

- **Two directional best arrays:** Compute shortest target intervals from the left and right, then split between positions. It remains linear but stores more structure.
- **Sliding window:** Positive values allow one moving window; combine found intervals with a prefix best value to reduce map usage.
- **Enumerate all interval pairs:** It repeats work and can become quadratic or worse.
- **Only one target interval:** No combination updates `ans`, so return `-1`.
- **Adjacent intervals:** They are non-overlapping and combine correctly when the left ends at `j` and right starts at `j+1`.
- **Nested target intervals:** Positive values strongly limit such patterns, and boundary-based combination still prevents overlap.
- **Target at the first element:** The initial zero prefix detects it.
- **Single-element intervals:** Their length one is stored normally.
- **Several candidate left intervals:** `f[j]` keeps the shortest, which is always best for total length.
- **Positive-values guarantee:** It makes prefix sums unique, though the map method also suggests extensions to broader inputs.
- **No answer:** Infinity survives and becomes `-1`.
- **Output bound:** Two non-overlapping subarray lengths sum to at most `N`.
- **Prefix-map timing:** The current prefix is inserted only after testing `s-target`, so a zero-length current interval can never be invented.
- **Carried prefix best:** Even when no interval ends at `i`, `f[i-1]` remains available for future right intervals.
