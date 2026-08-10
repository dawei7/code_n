## General

**Eliminate complete value groups as cheaply as possible.** A distinct integer disappears only after every occurrence of it is removed. Spending removals on part of a frequency does not reduce the unique count. To eliminate the greatest number of distinct values, fully remove the smallest frequencies first.

`Counter(arr)` maps each value to its occurrence count. The actual integer identities no longer matter because the objective counts how many identities remain, not which ones.

The source sorts `cnt.values()` ascending. For each frequency `v`, it subtracts `v` from remaining budget `k`, conceptually trying to erase that whole value group.

If `k` remains nonnegative, the group was fully removed. If it becomes negative, the budget was insufficient for the current group. That value and every not-yet-processed value remain distinct.

At sorted index `i`, there are `len(cnt)-i` such groups including the current one, which is exactly what the method returns.

If all frequencies fit, every occurrence has been removed and zero unique integers remain.

**Why smallest-first is optimal.** Suppose a strategy completely removes a frequency `b` while leaving a smaller frequency `a`, where `a <= b`. Replacing the removal of `b` with removal of `a` costs no more and eliminates the same one unique value, possibly leaving extra budget. Repeating this exchange transforms an optimal strategy into sorted-frequency order without worsening it.

Therefore the greedy prefix of smallest frequencies removes the maximum number of distinct values for the budget.

**Exactly k removals do not break the argument.** Once no additional group can be fully erased, any leftover removals may be taken from a remaining group without changing how many distinct values remain, unless the budget exactly completes it—which the loop already handles. The greedy count is valid for exactly, not merely at most, `k` removals.

For frequencies one, two, and three with `k=3`, the first two groups disappear exactly and one group remains. With `k=2`, the size-one group disappears and one occurrence can be removed from the size-two group, leaving two distinct values; overspending detection returns that count.

**Interpret the loop index precisely.** `enumerate` starts at zero. Before iteration `i`, all frequency groups at indices below `i` have been completely removed. The attempted subtraction of the current `v` determines whether group `i` can join them. If it cannot, remaining groups are indices `i` through `U-1`, a total of `U-i`. This is why the return expression includes the current group rather than subtracting one more.

The code temporarily lets `k` become negative instead of checking `k < v` first. Both forms are equivalent. A negative result is only a signal that the attempted whole-group removal must not be counted; no actual array mutation has happened, so there is nothing to undo.

**Why partially removing a cheapest remaining group is harmless.** When fewer than `v` removals remain, spending them anywhere among remaining occurrences cannot erase a frequency group whose size is at least `v`. The unique count is therefore fixed. It is valid to stop immediately rather than simulate those mandatory leftover deletions.

**Counter preserves multiplicity exactly.** Hash keys identify values, and their counts record every occurrence. Sorting only the counts intentionally forgets identities: exchanging the names of two groups with equal or different frequencies cannot change how many distinct values a given removal budget can eliminate.

**A tie example.** With frequencies two, two, and five and budget four, either order of the two size-two groups removes both, leaving one unique value. Stable ordering or original value order has no effect on the optimum.

## Complexity detail

Let `N` be array length and `U` the number of unique values. Building the counter takes expected `O(N)` time and `O(U)` space.

Sorting `U` frequencies takes `O(U log U)` time and `O(U)` Python sorting workspace. The scan is `O(U)`. Exact total time is `O(N + U log U)`, bounded by the manifest's looser `O(N log U)` notation.

The counter and sorted frequency list use `O(U)` space, matching the manifest.

## Alternatives and edge cases

- **Min-heap frequencies:** Pop cheapest groups until budget is insufficient. It has similar logarithmic processing.
- **Frequency-of-frequencies array:** Counts are at most `N`, enabling linear-time bucket processing with `O(N)` space.
- **Remove largest frequencies first:** This wastes budget and can leave more unique values.
- **k equals zero:** The first attempted subtraction becomes negative, returning all unique values.
- **k equals N:** Every group is removed and zero is returned.
- **One unique value:** It remains unless all its occurrences are removed.
- **All values unique:** Every frequency is one, so exactly `k` distinct values disappear.
- **Budget exactly matches a group:** `k` becomes zero and that group is correctly removed.
- **Partial current group:** It remains unique and is included in `len(cnt)-i`.
- **Tied frequencies:** Their order is irrelevant because their removal cost is equal.
- **Large integer values:** Hashing handles them without a bounded value array.
- **Input preservation:** Counter construction and sorting frequencies do not mutate `arr`.
- **Budget smaller than every frequency:** No value can disappear, so the original unique count is returned.
- **Partial removals are still required:** They can be spent after the greedy stopping point without decreasing the unique count.
- **Counter expected complexity:** The analysis assumes standard expected constant-time hashing.
- **Return zero:** It occurs only after every complete frequency group fits within the original removal budget.
