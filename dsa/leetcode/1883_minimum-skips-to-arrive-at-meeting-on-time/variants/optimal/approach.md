## General

**A skip changes the time carried into every later road.** Choosing whether to rest after one road cannot be judged in isolation. Skipping may let the fractional part of that road combine with a later road and land exactly on an integer hour, while resting rounds the accumulated time upward immediately. Dynamic programming is appropriate because the only history that matters after a prefix of roads is how many rests were skipped and the earliest arrival time achieved with that count.

**Define the full table.** `f[i][j]` is the minimum time after traveling the first `i` roads when exactly `j` post-road waits have been skipped in the recurrence. The table has `n + 1` rows and columns, initialized to `inf`. `f[0][0] = 0` is the only feasible empty journey: before taking a road, zero time and zero skips have been used. States with `j > i` cannot be reached and remain infinite.

**Transition when the current rest is not skipped.** For road length `x`, travel takes `x / speed` hours. If the traveler does not skip after it, departure for the next road is at the next integer hour, so the new time is the ceiling of the previous best time plus this duration:

`ceil(f[i - 1][j] + x / speed - eps)`.

This transition keeps the skip count `j`. The condition `j < i` avoids considering a no-skip transition into the state where all `i` rests are counted as skipped. It also ensures that at least one non-skipped choice exists in the path represented by those states.

**Transition when the wait is skipped.** If `j > 0`, the recurrence can use one of those skips on the current road. It comes from `f[i - 1][j - 1]`, adds `x / speed`, and performs no ceiling:

`f[i - 1][j - 1] + x / speed`.

The method takes the minimum of the skip and no-skip possibilities. Different earlier skip placements can reach the same `(i, j)` state, but only the earliest time can ever help future roads: all future operations add the same durations and apply monotone ceilings, so a later arrival cannot overtake an earlier one. Discarding every larger time is therefore safe.

**Why the final-road rounding does not change feasibility.** The physical journey requires no rest after the last road, yet the no-skip branch still applies `ceil` on row `n`. The deadline `hoursBefore` is an integer. For any real arrival time `t` and integer deadline `H`, `t <= H` exactly when `ceil(t) <= H`, aside from corrected floating error. Rounding final arrival upward can change its displayed value but cannot change whether it is at most the integer deadline. The skip branch also exists on the final row, but an unnecessary final skip cannot become necessary for a smaller answer: if unrounded time with that same earlier skip count meets integer `H`, the rounded no-final-skip state also meets it. Thus scanning for the smallest feasible `j` still returns the true minimum number of meaningful skipped rests.

**Use epsilon to protect exact integer boundaries.** Binary floating-point may represent a mathematically integral value such as two hours as `2.0000000000000004`. Applying `ceil` directly would incorrectly round it to three. The source subtracts `eps = 1e-8` before each ceiling, so tiny positive representation noise does not create a false waiting hour. The final check allows `hoursBefore + eps` for the same reason. This is a practical tolerance chosen for the bounded number and size of operations.

**Trace the first example.** With `dist = [1, 3, 2]` and speed four, the durations are `0.25`, `0.75`, and `0.5`. With no skips, the table rounds after the first road to one, after the second to two, and after the final to three, which is infeasible for deadline two. With one skip used after the first road, the prefix after two roads reaches exactly one hour; processing the last road and the no-skip rounding produces two, which is feasible. Although actual arrival is `1.5`, rounded value two has the same relation to the integer deadline. Therefore the ascending scan returns one.

**Find the minimum rather than merely any feasible count.** After filling all rows, the source checks `j = 0, 1, ..., n` in increasing order. The first `f[n][j] <= hoursBefore + eps` is returned immediately. Because each state is the best time for exactly that count, no smaller unchecked skip count exists, and every smaller checked count was infeasible. If even the all-skipped state fails, total raw travel time exceeds the deadline and the method returns `-1`.

**Why the recurrence covers every schedule.** For any plan over the first `i` roads using `j` skips, its choice after road `i` is either rest or skip. Removing that final choice leaves exactly one predecessor represented in row `i - 1`. Both categories are enumerated by the transitions. Conversely, extending a feasible predecessor with the corresponding travel and rounding rule forms a valid plan. Induction from `f[0][0]` proves that every table entry stores the earliest possible time for its exact skip count, which makes the final ascending feasibility scan correct.

## Complexity detail

For row `i`, the inner loop considers `i + 1` skip counts and performs constant work per state. Summing over all rows gives $O(n^2)$ time, matching the manifest. The final scan is only $O(n)$.

The exact source allocates an `(n + 1)` by `(n + 1)` table, so its auxiliary space is $O(n^2)$. This differs from the manifest's $O(n)$ space bound. Because a row depends only on the preceding row, the recurrence can be implemented with two length-$n+1$ arrays, or carefully updated one-dimensionally, to achieve $O(n)$ space. That optimization is not present in the checked-in implementation.

The table contains floating-point times, and `inf` provides the unreachable sentinel. Arithmetic involving `inf` remains infinite, so impossible predecessors cannot create finite states. With $n\le1000$, the quadratic table contains about one million entries plus Python list overhead, which is material but finite.

## Alternatives and edge cases

- **Integer distance units:** Store elapsed numerator units scaled by `speed` and round with integer arithmetic, for example to the next multiple of `speed`. This avoids epsilon reasoning entirely and is generally more robust than floating point.
- **Rolling-row DP:** Preserve only the previous and current rows to reduce auxiliary space from $O(n^2)$ to $O(n)$ while keeping $O(n^2)$ time and the same state meaning.
- **Greedy skipping of the largest wait:** The size of a wait depends on accumulated fractional time and later combinations, so locally largest current waits do not necessarily form a globally optimal set. DP captures these interactions.
- **One road:** There is no meaningful rest to skip. The rounded final arrival is feasible exactly when the real travel time meets the integer deadline, so the scan returns zero or `-1`.
- **Road ending at an exact integer hour:** Subtracting `eps` prevents harmless floating noise from causing an extra hour of rest.
- **All rests skipped:** The state `f[n][n]` represents uninterrupted raw travel and supplies the ultimate feasibility check. If it exceeds the deadline, no schedule can succeed.
- **Deadline reached exactly:** The `<=` comparison accepts exact arrival, as required, and the epsilon permits tiny numerical overshoot caused solely by representation.
- **Final road has no rest:** The source's ceiling is safe only because `hoursBefore` is an integer and the goal is feasibility, not the exact reported arrival time. A noninteger deadline or a task asking for exact time would require treating the last road separately.
- **Manifest space label:** The algorithmic recurrence admits linear-space compression, but the exact full table uses quadratic memory. The explanation should not conflate the optimized possibility with the executed source.
