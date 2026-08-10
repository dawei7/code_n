## General

**Store food metadata and cuisine rankings separately**

The system needs to locate a food's current rating and cuisine during updates, and retrieve the best item within one cuisine.

The exact source maintains:

- `self.g[food] = (rating, cuisine)`;
- `self.d[cuisine]` as a `SortedList` of ordering tuples for that cuisine.

Each ordering tuple is `(-rating, food)`. Python tuple ordering first compares the negative rating, then the food name.

**Why negate the rating**

`SortedList` orders ascending. A larger real rating produces a smaller negative number, so the highest-rated food appears first.

If ratings tie, the first tuple fields are equal and normal string ordering compares food names. The lexicographically smaller name comes first, exactly matching the tie-break.

Thus `self.d[cuisine][0]` is always the correct best tuple.

**Initialize every food in both structures**

The constructor zips `foods`, `cuisines`, and `ratings` so corresponding entries are processed together.

It inserts `(-rating, food)` into the cuisine's sorted list and records `(rating,cuisine)` under the unique food name.

After initialization, every food appears once in its cuisine list and once in the metadata map. Distinct food names make the map unambiguous.

**Change a rating with eager removal and insertion**

`changeRating` reads `oldRating, cuisine = self.g[food]`. The contract guarantees the food exists.

It updates the metadata to the new rating, removes exact tuple `(-oldRating, food)` from the cuisine list, and adds `(-newRating, food)`.

Removal is necessary because leaving the old tuple would create two rankings for one food. Unlike a lazy heap design, this structure contains only current entries.

The food's cuisine never changes, so it is removed and inserted within the same sorted list.

If the new rating equals the old rating, remove and add restore the identical state. The operation is correct despite doing redundant work.

**Return the first sorted food**

`highestRated(cuisine)` returns `self.d[cuisine][0][1]`. Index zero gives the smallest ordering tuple, and field one is the food name.

Every queried cuisine is guaranteed to contain at least one food, so the index is safe. No cleanup or scan is needed because updates eagerly preserve sorted order.

**State invariant and correctness**

After every operation, for each food `f` with metadata `(r,c)`, cuisine list `d[c]` contains exactly tuple `(-r,f)` and no stale tuple for `f`.

The invariant holds after construction. A rating change removes the one old tuple and installs the one new tuple while updating metadata. No other food changes.

Given the invariant, ascending tuple order places maximum rating first through negation. Among equal ratings it places the lexicographically smallest name first. Therefore every highest-rated query is correct.

**The exact source is not a lazily cleaned heap**

The manifest summary describes pushing new heap entries and later discarding stale ratings. The source instead uses `SortedList.remove` and `add` eagerly. Space remains proportional to current foods rather than update history, and query needs no validation loop.

## Complexity detail

Let `n` be the number of foods and `q` the number of calls. Each constructor insertion into a cuisine's sorted list costs up to `O(\log n)` plus library movement costs, giving a conservative `O(n \log n)` initialization.

A rating change performs one sorted removal and one insertion, conventionally `O(\log n)` search with the `SortedList` library's block-based update costs. Retrieving index zero is constant or logarithmic depending on library accounting; it is at most `O(\log n)`.

Metadata and cuisine lists store one current entry per food, so space is `O(n)`, not `O(n+q)` stale history. Cuisine and food strings are existing input objects referenced by maps and tuples.

## Alternatives and edge cases

- **Heap with lazy deletion:** Push every new `(-rating,food)` tuple and compare heap tops with current metadata during queries. Updates are simple, but stale entries accumulate to `O(n+q)` space.
- **Scan all foods in a cuisine per query:** Updates are easy, but queries can become linear in cuisine size.
- **Sort a cuisine list after every update:** Resorting costs `O(n \log n)` per change rather than maintaining order incrementally.
- **Use positive ratings in ascending order:** The lowest-rated food would appear first. Negation reverses rating priority.
- **Negate the food name:** Strings do not need reversal; ordinary lexicographic ascending is the required tie-break.
- **Tie after an update:** Equal negative ratings cause names to decide order automatically.
- **New rating equals old:** Remove and reinsert the same tuple without changing results.
- **Only one food in a cuisine:** It is always returned.
- **Food names are unique:** Exact tuple removal and metadata lookup are unambiguous.
- **Cuisine never changes:** The API modifies only ratings, so metadata retains its original cuisine.
- **Guaranteed cuisine query:** Index zero is safe because every queried cuisine has at least one food.
- **External dependency:** The source requires `SortedList` from its supporting library.
- **Persistent mutation:** Internal ranking structures intentionally change across calls; input arrays are only read during construction.
