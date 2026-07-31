## General

Let $c=\texttt{candidates}$. Only workers exposed at the two ends can be hired. Put the first $c$ workers and the non-overlapping portion of the last $c$ workers into one min-heap. Store `(cost, original index, side)` for each entry. Tuple order enforces both selection rules: cost is primary and original index breaks ties. Removing workers preserves the relative order of those who remain, so comparing original indices is equivalent to comparing their current indices.

**Representing the unexposed middle.** Keep `left` and `right` at the first and last workers not yet placed in the heap. After popping a worker, expose one replacement from the same side, provided `left <= right`. This maintains the invariant that the heap contains exactly the first and last $c$ available workers, except when fewer remain, when it contains every remaining worker.

The right initial range begins at `max(candidates, n - candidates)`. This prevents overlapping candidate regions from inserting the same worker twice. Each session therefore pops exactly the worker prescribed by cost and index, adds its cost once, and restores the candidate boundary for the next session.

## Complexity detail

Let $c=\texttt{candidates}$. Initializing and heapifying at most $2c$ entries takes $O(c)$ time. Each of the $k$ sessions performs one pop and at most one push on a heap of size at most $2c$, so total time is $O((c+k)\log c)$.

The heap contains at most $2c$ workers and all remaining state is scalar, giving $O(c)$ auxiliary space.

## Alternatives and edge cases

- **Two min-heaps:** Separate left and right heaps achieve the same bound; ties must choose the left heap because every exposed left index precedes every exposed right index.
- **Repeated candidate scan:** Materializing and scanning both candidate regions each session is correct but can take $O(kc)$ time.
- **Globally sort workers:** Sorting all costs ignores that an inexpensive middle worker is unavailable until its side advances.
- **Overlapping regions:** When $2c>n$, each worker must be inserted only once rather than appearing in both candidate pools.
- **Tie breaking:** Heap entries include the original index so equal costs select the smallest remaining index.
- **Exhausted middle:** Once `left > right`, no replacement is pushed; the heap already contains every worker still available.
- **Single worker:** With $n=k=c=1$, the lone heap entry is selected and no replenishment occurs.
