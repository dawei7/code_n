## General

**Translate race order into a position lookup**

`order` lists every participant in finishing order. The index of an ID is therefore its finishing rank: a smaller index means the participant finished earlier.

The source builds

`d = {x: i for i, x in enumerate(order)}`.

For every participant ID `x`, `d[x]` is the zero-based position where that participant appears in the race result.

The permutation guarantee makes the mapping unambiguous. Every ID from one through `n` appears exactly once, so no dictionary entry is overwritten by a duplicate.

**Sort only the friends by their race positions**

The input `friends` is sorted by numeric ID, but numeric ID has no relationship to finishing time. The desired output orders these same IDs by `d[x]`.

The source returns

`sorted(friends, key=lambda x: d[x])`.

The key function replaces each friend only for comparison with that friend’s race position. The returned list still contains the original IDs.

Every friend is guaranteed to appear in `order`, so all dictionary lookups succeed. No missing-ID branch is needed.

**Why the result is correct**

Take any two friends `a` and `b`. If `a` finished before `b`, then `d[a] < d[b]`. Key sorting therefore places `a` before `b`.

This pairwise property holds for every pair of friends, so the complete sorted result has exactly the same relative order as their occurrences in `order`.

Every input friend appears once in the returned list because `sorted` rearranges rather than filters. No non-friend can appear because the source sorts only `friends`.

**Trace the first example**

For `order = [3, 1, 2, 5, 4]`, the position map contains:

- `3 -> 0`
- `1 -> 1`
- `2 -> 2`
- `5 -> 3`
- `4 -> 4`

The friend IDs `[1, 3, 4]` have keys one, zero, and four. Sorting by those keys gives `[3, 1, 4]`.

**Why the original increasing order of `friends` is irrelevant**

Strictly increasing friend IDs are useful as an input guarantee but do not solve the task. A participant with a larger ID can finish earlier. The method deliberately ignores the original friend ordering and uses only race positions as comparison keys.

Python’s sort is stable, but stability is not important here because two distinct friends cannot have the same finishing position.

**The exact source differs from the manifest summary**

The manifest describes placing the at-most-eight friend IDs in a set and filtering `order` in one stable pass. That would run in `O(n)` time and use `O(1)` space under the fixed `friends.length <= 8` bound.

The exact source instead builds a dictionary entry for every participant, which uses `O(n)` space, and sorts the friend list by positions. Its general time is

`O(n + f log f)`,

where `f = len(friends)`.

Since `f <= 8`, the sorting term is bounded by a small constant and total time simplifies to `O(n)` under the constraints. The space does not simplify to `O(1)` because the position dictionary still grows with `n`.

The source remains correct and efficient; it simply implements a different tradeoff from the manifest’s stated filter.

**Why a position map can still be useful**

If many different friend subsets were queried against the same race order, building `d` once would let each subset be sorted without rescanning all `n` finishers. For this one-query problem with at most eight friends, filtering is leaner, but the mapping approach is direct and general.

The method creates a new output list. Neither `order` nor `friends` is modified.

## Complexity detail

Let `n = len(order)` and `f = len(friends)`.

Building the dictionary takes expected `O(n)` time. Sorting `f` friends takes `O(f log f)` comparisons, and each key lookup is expected `O(1)`. Total expected time is `O(n + f log f)`.

With `f <= 8`, this is `O(n)` for the stated input domain.

The dictionary stores `n` entries and the returned sorted list contains `f` elements. Exact-source auxiliary storage is `O(n + f) = O(n)`, not the manifest’s `O(1)`.

## Alternatives and edge cases

- **Filter `order` with a friend set:** Build a set of the at-most-eight IDs and retain finishers belonging to it. This matches the manifest’s `O(n)` time and bounded `O(1)` auxiliary space.
- **Call `order.index` for each friend:** It avoids a map but scans up to `n` elements per friend, costing `O(nf)`; with `f <= 8` it is still linear up to a constant but less scalable.
- **Sort friends by ID:** They are already ID-sorted, which does not represent finishing order.
- **Sort the complete order:** `order` already has the desired ranking; sorting it numerically would destroy that information.
- **One friend:** The returned list contains that same ID.
- **All participants are friends:** Sorting by positions reconstructs `order` exactly.
- **Friend who finished first or last:** Position keys zero and `n - 1` place them at the appropriate ends.
- **Duplicate friend IDs:** The constraints say `friends` is strictly increasing, so duplicates do not occur.
- **Missing friend ID:** The contract guarantees membership. Without it, `d[x]` would raise `KeyError`.
- **Input preservation:** `sorted` returns a new list, and dictionary construction does not mutate either input.
- **Missing import:** The stored source uses `List` without importing it. Standalone Python needs `from typing import List` unless the harness provides the name.
