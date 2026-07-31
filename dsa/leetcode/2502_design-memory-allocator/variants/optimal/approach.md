## General

**Model every memory unit explicitly**

Keep an array of length $n$ whose value is `0` for a free unit and otherwise is the owning `mID`. This representation records exactly the state queried by both operations and naturally supports several disjoint blocks with the same identifier.

For allocation, scan from left to right while counting the current consecutive run of zeroes. An occupied unit resets the count. The first time the count reaches `size`, the run is necessarily the leftmost valid block: every earlier scan position has already been shown not to end such a run. Fill that block with `mID` and return its start. Reaching the end without a long enough run proves that allocation must fail, and no state has been changed.

For `freeMemory`, scan all units. Replace every occurrence of the requested `mID` with `0` and count the replacements. Inspecting the complete array is essential because one identifier may own several non-adjacent blocks. The returned count is therefore exactly the amount released.

## Complexity detail

Let $n$ be the memory size and $q$ the number of method calls after construction. Each `allocate` scan costs $O(n)$; filling its successful block costs at most another $O(n)$. Each `freeMemory` call also costs $O(n)$. The complete operation sequence therefore costs $O(qn)$ time, and the ownership array uses $O(n)$ space.

The output list used by the app-local adapter is part of the calling harness rather than allocator state and is excluded from the branch's auxiliary-space bound.

## Alternatives and edge cases

- **Test every candidate slice:** Checking `memory[start:start + size]` for every start is simple but copies or scans up to `size` elements per candidate, giving $O(n^2)$ time for one allocation.
- **Interval or segment tree structures:** More advanced free-interval tracking can improve operation costs for larger constraints, but it adds substantial update and merging complexity that the $n,q\le1000$ contract does not require.
- **Repeated `mID`:** Allocation never assumes identifier uniqueness; a later free clears every matching unit across all blocks.
- **Fragmentation:** The allocator requires one consecutive run, so enough free units in total do not guarantee success.
- **Failed allocation:** State is written only after a complete run is found, so failure leaves all ownership unchanged.
- **Missing identifier:** A free scan that finds no matching unit returns `0`.
