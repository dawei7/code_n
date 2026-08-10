## General

**Binary-search a monotone deadline.** If all indices can be marked within the first $t$ seconds, the same schedule remains possible with any later deadline by doing nothing in extra seconds. Feasibility is therefore false for an initial range of deadlines and true afterward. The source binary-searches the first true value.

**Reserve the last occurrence for each mark.** For a chosen prefix `changeIndices[:t]`, an index can be marked only at a second where it appears. If we decide to mark it by time $t$, using its last occurrence is never worse: this leaves the greatest possible number of earlier seconds for required decrements.

Dictionary `last` maps each appearing one-indexed array index to its last zero-based second within the prefix. The comprehension overwrites earlier occurrences to obtain that final position.

**Treat every non-reserved second as decrement capacity.** Scan the prefix chronologically. Variable `decrement` counts unallocated seconds that are not reserved as last-occurrence marks.

When the current occurrence is not the last for its index, the second may be used to decrement any array element, so `decrement` increases by one.

When it is the last occurrence of index `i`, that second must be used to mark `i`. Before marking, `nums[i - 1]` decrements must have occurred. If the available pool is smaller, no valid schedule can meet this deadline and `check` returns false. Otherwise the source subtracts that many slots and increments `marked`.

**Why a pooled count is enough.** A decrement operation may target any index, independently of `changeIndices[s]`. Therefore earlier free seconds are interchangeable. At a marking deadline, only their total count matters. Allocating `nums[i-1]` slots to the index is sufficient; their exact order among earlier free seconds can be chosen afterward.

**Why failure at a last occurrence is conclusive.** Later seconds in the tested prefix cannot help mark this index because the current occurrence is its last. Decrements performed after it would also be too late for its mark. If the accumulated earlier capacity is insufficient, no rearrangement can fix the schedule.

**Require every index to appear.** Even if all encountered deadlines were affordable, an array index absent from the prefix cannot be marked. Returning `marked == len(nums)` enforces that every index had a reserved last occurrence.

**Binary-search mechanics.** The source calls `bisect_left` over values 1 through $m+1$ with `key=check` and target `True`. This locates the first feasible deadline. The extra $m+1$ acts as a sentinel; slicing at that value still uses the whole schedule. The resulting position is converted back to the one-based deadline by adding one. If it exceeds $m$, the method returns $-1$.

**A schedule interpretation.** In a feasible prefix, every last occurrence consumes one mark second, and earlier non-last occurrences supply decrement seconds. The chronological pool test ensures every mark's decrement work fits before its deadline. Since decrements are freely assignable, the aggregate reservation can be expanded into an actual schedule.

## Complexity detail

One `check(t)` call slices and scans up to $t$ change entries and builds a dictionary with at most $N$ keys, costing $O(t+N)$ time in the broad bound. Binary search makes $O(\log M)$ checks, yielding $O((N+M)\log M)$ time.

The dictionary uses $O(N)$ entries, but the exact source also creates `changeIndices[:t]` twice—once for the comprehension and once for the scan. The temporary slice alive during scanning can hold $O(M)$ references. Peak auxiliary space is therefore $O(N+M)$, rather than strictly $O(N)$ when the parameters are independent.

The inputs are not modified.

## Alternatives and edge cases

- **Linear test of every deadline:** Repeating feasibility for all $M$ prefixes costs $O(M^2)$ time; monotonicity supports binary search.
- **Use first rather than last occurrence for marking:** It wastes possible earlier decrement time and can falsely declare a feasible prefix impossible.
- **Explicitly assign decrement seconds to indices:** A total pool suffices because any free second may decrement any index.
- **Index absent from prefix:** `marked` remains below $N$, so feasibility is false even if its initial value is zero.
- **Zero-valued index:** It requires no decrement slots but still needs one occurrence to mark.
- **Repeated occurrences:** Only the last is reserved; earlier ones optimally become decrement capacity.
- **Deadline one:** It is feasible only in the narrow situation where the one second can mark the sole zero-valued index.
- **Impossible full schedule:** Binary search reaches beyond $M$ and returns $-1$.
- **Do-nothing operation:** It never improves feasibility while work remains, so free seconds can be viewed as decrement capacity; unused capacity is harmless.
- **Slice space:** The protected Python source allocates prefix lists, so its exact peak space exceeds the manifest's dictionary-only description.
- **Why decrement values never go below zero in the constructed schedule:** The feasibility test allocates exactly `nums[i]` decrements before marking index $i$. Extra pooled seconds may remain unused, so there is never a reason to decrement an already prepared value further.
- **Binary-search key requirement:** This source relies on Python's `bisect_left(..., key=...)` support. The searched sequence is virtual deadline values, while `check` supplies their monotone Boolean keys.
