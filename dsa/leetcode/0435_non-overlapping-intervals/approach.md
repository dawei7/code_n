## General

**Minimize removals by maximizing intervals kept**

If there are $n$ intervals and a non-overlapping subset of size $K$ is retained, exactly $n-K$ intervals are removed. Therefore minimizing removals is equivalent to choosing the largest possible collection of mutually non-overlapping intervals.

This is the interval-scheduling problem. The optimal greedy choice is always to keep the currently available interval that ends earliest. An earlier finishing interval leaves at least as much room as a later finishing one for every future interval.

The solution sorts `intervals` in ascending order of their end coordinate with

`intervals.sort(key=lambda x: x[1])`.

It then scans in that order, keeping every interval whose start does not overlap the end of the most recently kept interval.

**Track the end of the kept schedule**

`pre` is the end coordinate of the last interval accepted. It begins at negative infinity, so the first sorted interval is always eligible.

For current interval `[l,r]`, the condition `pre <= l` means the interval begins at or after the preceding kept interval ends. Equality is allowed because the contract says intervals touching at one point are non-overlapping.

When the condition holds, the interval is kept and `pre` becomes `r`. When it fails, the interval overlaps the kept schedule and is skipped.

Because intervals are sorted by end time, a skipped current interval cannot end earlier than the most recently kept interval. Replacing the kept interval with the current one would not improve the boundary for future choices.

**Why `ans` starts at the total size**

Instead of counting removals directly, the exact code initializes `ans = len(intervals)`. Every time an interval is kept, it executes `ans -= 1`.

After the scan,

`ans = total intervals - kept intervals`,

which is exactly the number removed. Skipped intervals require no explicit increment because they remain included in the initial total.

For `[[1,2],[2,3],[3,4],[1,3]]`, sorting by end produces an order beginning with `[1,2]`. It is kept, `[2,3]` is allowed because it touches at 2, and `[3,4]` is allowed. `[1,3]` overlaps the established boundary when encountered and is skipped. Three are kept from four, so `ans` finishes at one.

**The exchange argument behind earliest finish**

Consider an optimal non-overlapping schedule and let its first selected interval end at $E$. The greedy algorithm selects an interval ending at $G$, where $G \le E$ because it chooses the earliest end among all candidates.

Replace the optimal schedule's first interval with the greedy interval. Every later interval started at or after $E$; since $G \le E$, it also starts at or after $G$. The replacement creates no overlap and preserves the number of selected intervals.

Thus some optimal schedule begins with the greedy choice. Remove that chosen interval and apply the same argument to intervals beginning at or after its end. By induction, every greedy choice can be part of an optimal maximum-size schedule. The scan therefore keeps as many intervals as possible, and `n - kept` is the minimum removal count.

**Why sorting by start time would not support the same rule**

An interval that begins earliest may extend very far and block many short intervals. End time measures how much future space a choice leaves. That is the quantity the exchange proof depends on.

For example, keeping `[1,100]` because it starts first would block `[2,3]`, `[3,4]`, and many others. Earliest-finish sorting chooses the short opportunities instead.

**Input mutation**

Python's list `.sort()` rearranges `intervals` in place. The function contract asks only for the removal count, so preserving original order is unnecessary for this solution. If callers required the input unchanged, `sorted(...)` could create a separate list at an additional $O(n)$ reference cost.

## Complexity detail

Let $n$ be the number of intervals. Sorting costs $O(n\log n)$ time, and the subsequent scan costs $O(n)$. Total time is $O(n\log n)$.

Python's Timsort can use $O(n)$ temporary memory in the worst case, matching the manifest's $O(n)$ space bound. The greedy scan itself uses only `ans`, `pre`, and current endpoints, or $O(1)$ additional state beyond sorting.

## Alternatives and edge cases

- **Dynamic programming:** After sorting, compute the maximum compatible subset with predecessor searches. It is correct but unnecessarily heavier than the greedy exchange property.
- **Sort by start and keep the smaller end on overlap:** This can also implement the same greedy idea: whenever two intervals overlap, discard the one ending later. Earliest-end sorting makes the invariant simpler.
- **Remove the shortest interval on overlap:** Shortest duration is not the right measure; absolute finishing time determines future compatibility.
- **Brute-force subsets:** Testing all keep/remove combinations is exponential.
- **Touching intervals:** `pre <= l` deliberately accepts `[1,2]` followed by `[2,3]`.
- **Duplicate intervals:** Only one copy can be kept when they overlap exactly; the rest remain counted as removals.
- **Nested intervals:** The one with the earlier end is favored, even if it starts later, because it leaves more future room.
- **Negative coordinates:** Negative infinity initialization and ordinary comparisons handle them without a special case.
- **One interval:** It is kept, reducing `ans` from one to zero.
- **Already non-overlapping input:** Every interval is kept after sorting, so the answer becomes zero.
- **All intervals overlap:** Greedy keeps one earliest-ending interval, and the result is $n-1$ removals.
