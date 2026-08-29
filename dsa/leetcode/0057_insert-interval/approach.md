## General

**Reduce insertion to ordinary interval merging**

The input intervals are already sorted and non-overlapping, so a specialized solution can insert in linear time. The selected source takes a simpler but less efficient route: append `newInterval` to the list, sort all intervals, and then run the standard merge-interval scan.

Once sorted, starts are non-decreasing. The merge helper keeps a result whose last interval represents the active overlapping chain. Each new interval either begins after that active end, creating a gap, or overlaps it and extends the active end.

**What sorting establishes**

`intervals.sort()` orders each two-element list lexicographically, first by start and then by end. Even though the original input was sorted, appending an arbitrary new interval can break that order. Sorting restores it.

After sorting, when a new start is greater than the last merged end, no later interval can overlap that result interval because later starts are at least as large. This makes finalization safe.

**Initialize from the first sorted interval**

`ans = [intervals[0]]` starts the merged result with the first interval object. The combined list can never be empty: even if original `intervals` is empty, the public method appends `newInterval` before calling `merge`. Therefore, indexing position 0 is safe for every valid input.

This initialization stores an alias to an existing inner list rather than a copy. That has mutation consequences described below.

**Gap versus overlap for closed intervals**

For each later `[s,e]`, the test `ans[-1][1] < s` checks for a strict gap. If the active end is smaller than the new start, `[s,e]` begins a separate interval and a fresh list is appended.

Otherwise, the intervals overlap or touch. Equality counts as overlap because the intervals are closed and share the endpoint. The source keeps the existing start and updates the active end to `max(ans[-1][1], e)`. A contained interval leaves the end unchanged; an extending interval enlarges it.

**The merge invariant**

After processing a sorted prefix, `ans` is sorted, its intervals are pairwise non-overlapping, and their union equals the union of that prefix. Only the final result interval could overlap the next sorted input.

A strict gap appends a new non-overlapping group. An overlap expands the final group to exactly the union of itself and the new interval. No earlier group can become involved because sorting places the active group between earlier ends and all future starts.

At loop completion, the invariant covers every original interval plus `newInterval`, so `ans` is the correct inserted-and-merged union.

**Example through append, sort, and merge**

For `[[1,2],[3,5],[6,7],[8,10],[12,16]]` and `[4,8]`, appending places the new interval at the end temporarily. Sorting moves it between `[3,5]` and `[6,7]`. The merge scan keeps `[1,2]` separate, combines `[3,5]` with `[4,8]`, then absorbs `[6,7]` and `[8,10]`, producing `[3,10]`. `[12,16]` remains separate.

**Exact mutation and aliasing behavior**

The public method executes `intervals.append(newInterval)`, so the caller's outer list gains the exact `newInterval` object. `intervals.sort()` then reorders that outer list.

Inside `merge`, the first output entry is `intervals[0]` itself. If later intervals overlap it, assigning `ans[-1][1]` mutates that same original inner list. Later non-overlapping intervals are appended as fresh `[s,e]` lists, so they do not retain aliases. Consequently, which inner object is mutated depends on which interval sorts first and begins the first merged group.

This behavior is allowed because the note says in-place preservation is not required, but callers should not assume either input list remains unchanged.

**Why this is not the promised linear algorithm**

The source discards the useful precondition that original intervals are already sorted and disjoint. A three-phase scan can copy intervals left of the new one, merge the overlapping block, and copy the right suffix in $O(n)$ time. Sorting all $n+1$ intervals instead costs $O(n \log n)$, so the exact implementation does not meet the manifest's time claim.

## Complexity detail

Appending is amortized $O(1)$. Sorting $n+1$ intervals costs $O(n \log n)$. The slice `intervals[1:]` and merge scan each cost $O(n)$. Total time is therefore $O(n \log n)$, not the manifest's $O(n)$.

The returned answer may contain $O(n)$ intervals. The suffix slice allocates $O(n)$ references, and Python sorting may use $O(n)$ temporary workspace. Overall storage is $O(n)$, consistent with the manifest's space bound. Required output and auxiliary temporaries both fit that class.

## Alternatives and edge cases

- **Three-phase linear scan:** Append intervals strictly before `newInterval`, merge all overlaps, then append the remaining suffix. It uses the sorted/non-overlapping guarantee and achieves $O(n)$ time.
- **Binary search for insertion point:** Locate the starting neighborhood quickly, but merging and constructing the output can still require $O(n)$ time.
- **Non-mutating sort:** Use `sorted(intervals + [newInterval])` to preserve the outer input, at the cost of an explicit combined copy and the same sorting time.
- **Empty original list:** Appending first makes the merge input contain one interval, which is returned.
- **New interval before all others:** Sorting moves it to the front; it may become the aliased first output object.
- **New interval after all others:** Sorting leaves it last, and it is merged or appended according to endpoint overlap.
- **Touching endpoint:** Strict `<` treats equality as overlap, as required for closed intervals.
- **Contained new interval:** Merging may leave existing outer bounds unchanged, but the caller's outer list still contains the appended object.
- **Covers all intervals:** Repeated end extension creates one result interval spanning the entire union.
- **Input mutation:** The outer list is appended to and sorted, and the first inner interval may have its end changed through aliasing.
