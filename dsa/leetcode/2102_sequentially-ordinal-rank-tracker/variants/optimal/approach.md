## General

**Encode the complete ranking in one sortable tuple**

Locations rank by two rules:

1. higher score is better;
2. among equal scores, lexicographically smaller name is better.

`SortedList` maintains values in ascending tuple order. To make ascending order correspond to best-to-worst ranking, the source stores each location as

`(-score, name)`.

Negating the score reverses its direction: score 10 becomes -10 and appears before score 8, which becomes -8. When negated scores tie, normal tuple comparison moves to `name`, where lexicographically smaller strings already come first.

Therefore, index 0 of `self.sl` is always the best location, index 1 the second best, and so forth.

**Maintain the query ordinal, not a location pointer**

`self.i` starts at -1. Every `get()` first increments it:

`self.i += 1`.

On the first query it becomes 0, so the best location is returned. On the second it becomes 1, so the second-best location among everything added by that time is returned.

The query count is the rank requested by the problem. It is not the identity of a previously returned location.

This distinction matters when new locations are inserted between queries. An insertion can appear before the current rank and shift all later entries. Keeping an iterator to the previously returned object would not correctly identify the next ordinal in the newly ranked collection. Indexing the current sorted list with the persistent query number does.

**Adding a location**

`add(name, score)` inserts `(-score, name)` into the sorted structure. `SortedList.add` places it at the correct tuple position while preserving all earlier locations.

Names are unique, so two stored tuples cannot be identical. Scores may tie, and the name component gives the required deterministic order.

There is no need to adjust `self.i` during an addition. It records only how many calls to `get` have occurred. The next query's required ordinal increases by one regardless of where the new item ranks.

**Trace insertions between queries**

After adding `("bradford", 2)` and `("branford", 3)`, the stored order is

`[(-3, "branford"), (-2, "bradford")]`.

The first `get` changes `i` from -1 to 0 and returns `"branford"`.

Adding `("alps", 2)` inserts it before `"bradford"` because the scores tie and `"alps"` is lexicographically smaller. The current ranking is branford, alps, bradford. The second `get` sets `i = 1` and returns alps.

This shows why the structure must remain dynamically sorted rather than merely append new locations after earlier results.

**Why the algorithm is correct**

At all times, tuple ordering in `self.sl` exactly equals the stated best-to-worst ordering. This follows from the negated primary score and unchanged ascending secondary name.

Before the $q$th call to `get`, `self.i = q-2` because it began at -1 and was incremented once for each earlier query. Incrementing makes it $q-1$, the zero-based index of the $q$th-best location.

Returning the name component of that tuple therefore returns exactly the required location among all locations currently added.

The constraint that query count never exceeds add count ensures this index always exists.

**What `SortedList` contributes**

A plain Python list would require shifting elements during ordered insertion, which is linear. `SortedList` is a balanced, block-based ordered container supplied by the solution environment. It supports logarithmic-time insertion and indexed access at the scale represented by the manifest.

The exact method depends on this ordered-container facility rather than implementing its balancing internally.

## Complexity detail

Let $m$ be the number of locations currently stored.

`add` performs one ordered insertion in $O(\log m)$ time. `get` increments a counter and performs indexed access; under the `SortedList` complexity model this is $O(\log m)$, matching the manifest's per-operation bound.

The structure stores one tuple per added location, using $O(m)$ space. The query counter uses constant space.

Each name has bounded length under the constraints, so string comparisons contribute only a bounded factor here.

## Alternatives and edge cases

- **Sort all locations during every `get`:** Correct but repeats $O(m\log m)$ work per query. Maintaining order incrementally avoids full re-sorts.
- **Plain sorted list with binary search:** Finding an insertion point is logarithmic, but inserting into a Python list shifts $O(m)$ elements.
- **Two heaps:** A carefully balanced pair of heaps can track the requested rank and support efficient operations, but tie ordering and insertions around the boundary require more invariants.
- **Negating the wrong field:** Only score order is descending. Names must remain ascending for ties.
- **First query:** Incrementing from -1 to 0 returns the best location.
- **Insert before the current ordinal:** The next query uses the updated sorted order at its new ordinal, as required.
- **Equal scores:** Lexicographically smaller names appear first through tuple comparison.
- **Unique names:** No two locations are completely indistinguishable in the ordering.
- **Enough additions guarantee:** `self.sl[self.i]` cannot be out of range on valid operation sequences.
- **Return only the name:** The score is used for ranking but the contract requests the location name.
- **Persistent state:** Both the sorted collection and query counter must survive across method calls.
- **External ordered container:** The complexity claim assumes the provided `SortedList` implementation, not a built-in flat list.
