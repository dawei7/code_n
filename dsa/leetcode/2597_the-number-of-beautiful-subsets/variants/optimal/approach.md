## General

**Separate values that can never conflict.** Two integers whose difference is `k` have the same remainder modulo `k`. Values from different remainder groups are therefore independent, so their numbers of valid choices can be multiplied.

**Compress duplicate values.** If a value occurs $f$ times, selecting at least one of its copies can be done in $2^f-1$ index-distinct ways. Equal copies do not conflict with one another because `k` is positive. Sort the distinct values inside each remainder group; only values separated by exactly `k` are adjacent conflict candidates.

**Run a weighted path dynamic program.** For a group, keep the numbers of selections that do not take and do take the previous distinct value. If the current value is exactly `k` above the previous value, taking it is allowed only after a state that did not take the previous value. If the gap is larger, all previous states may be extended by any non-empty choice of current copies. Skipping the current value always preserves every previous state.

The two states enumerate all beautiful selections within a remainder group without overlap. Multiplying the completed group totals combines independent selections across remainders. This product includes the globally empty selection once, so subtract one to retain only non-empty subsets.

## Complexity detail

Let $n$ be the length of `nums`. Counting frequencies takes $O(n)$ time. Sorting all distinct values across their remainder groups costs at most $O(n \log n)$ time, and the dynamic-programming scans are linear. The frequency tables and grouped values use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Backtracking with selected-value counts:** Include or exclude each position while checking values `k` away. This is straightforward and source-aligned, but takes $O(2^n)$ time in the worst case.
- **Enumerate all bitmasks:** Testing every non-empty index subset is also exponential and repeats the same conflict checks many times.
- **Duplicate values:** All non-empty selections among $f$ equal copies contribute $2^f-1$ choices because their mutual difference is zero, not positive `k`.
- **Gaps larger than `k`:** They break a conflict chain, allowing the current value to extend both prior states.
- **Empty subset:** Each group DP includes choosing nothing; subtract exactly one only after multiplying all group totals.
