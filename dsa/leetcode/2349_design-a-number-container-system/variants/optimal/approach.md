## General

**Maintain both directions of the relationship**

The class must replace the value at an index and find the smallest index for a value. One mapping alone does not support both efficiently.

The exact solution stores:

- `self.d[index] = number` for the current content of every assigned index;
- `self.g[number]` as a `SortedSet` of all indices currently containing that number.

The first mapping identifies what must be removed during replacement. The second keeps candidate indices unique and ordered so the smallest is accessible.

**Change removes the old reverse association first**

If `index in self.d`, the index already contains `old_number = self.d[index]`. Before assigning the new value, the method executes

`self.g[old_number].remove(index)`.

This eager removal preserves the reverse-map invariant: after replacement, the old number's set no longer claims the index.

The implementation does not delete the number key when its sorted set becomes empty. Keeping an empty set is harmless because `find` checks truthiness.

If the new number equals the old number, the method removes the index and immediately adds it back. This is redundant work but leaves the state correct.

**Install the new forward and reverse associations**

`self.d[index] = number` records the current value. Then `self.g[number].add(index)` inserts the index into the new number's ordered set.

`SortedSet.add` is idempotent, so no duplicate index can appear. This matters for repeated identical `change` calls.

After these steps, the following invariant holds:

> index `i` belongs to `self.g[x]` exactly when `self.d[i] == x`.

**Find reads the minimum ordered index**

`ids = self.g[number]` retrieves the sorted set for the query value. Because `g` is a `defaultdict(SortedSet)`, querying an unseen number creates and returns an empty sorted set.

If `ids` is nonempty, `ids[0]` is its smallest element and therefore the smallest assigned index containing `number`. If empty, the method returns `-1`.

The creation of empty sets for unsuccessful queries is a small state side effect. With at most `q` calls, it still fits the overall linear space bound.

**Why both maps stay consistent**

Initially both maps are empty, so the invariant holds.

During `change`, any old reverse membership is removed before the forward value changes. The new forward mapping and reverse membership are then installed together. No other index or number relationship is touched.

By induction over changes, every sorted set contains exactly its current indices. `find` consequently returns a valid minimum and never a stale index.

**A replacement trace**

After changes `(2,10)`, `(1,10)`, and `(3,10)`, `g[10]` contains sorted indices `[1,2,3]` and `find(10)` returns 1.

Changing index 1 to 20 removes 1 from `g[10]`, changes `d[1]`, and adds 1 to `g[20]`. The next `find(10)` sees `[2,3]` and returns 2.

**The exact source is eager sorted-set maintenance**

The manifest summary mentions lazy stale-index cleanup with heaps. The provided source performs immediate removal from a `SortedSet`, so it contains no stale entries. This changes the method-level explanation and complexity constants even though aggregate bounds are similar.

## Complexity detail

Let `q` be the total number of operations and `r` the number of indices associated with a particular number. Hash-map lookup is expected `O(1)`. Sorted-set removal and insertion are `O(\log r)`, so `change` is `O(\log q)` in the worst case.

Retrieving `ids[0]` from the tree/list-backed `SortedSet` is commonly logarithmic in its size, so a conservative exact bound for `find` is `O(\log q)`, with expected constant hash lookup. Across all calls, `O(q \log q)` is safe.

Each assigned index appears once in `d` and once across nonempty reverse sets. Empty sets may also be created by distinct failed finds. Total storage is `O(q)`.

## Alternatives and edge cases

- **Min-heaps with lazy deletion:** Push every changed index into the new number's heap and use `d` to discard stale heap tops during find. Change avoids eager removal, but heaps may accumulate stale entries.
- **Unordered sets:** Replacement is easy, but finding the minimum requires scanning all indices for that number.
- **One global scan of `d` per find:** This uses less reverse structure but makes every query `O(q)`.
- **Change an unused index:** No old removal occurs; both new associations are inserted.
- **Replace with a different number:** The index disappears from the old set before entering the new set.
- **Replace with the same number:** Remove-then-add preserves state despite extra work.
- **Find an unseen number:** The default dictionary creates an empty set and returns `-1`.
- **Find a number whose set became empty:** Truthiness fails and `-1` is returned.
- **Several indices for one number:** Sorted order makes the least one appear at position zero.
- **Remove the current smallest through replacement:** The next ordered index automatically becomes the minimum.
- **Large sparse indices:** Storage depends on assigned indices, not on the numeric maximum `10^9`.
- **Duplicate reverse membership:** Sorted-set uniqueness prevents it.
- **External dependency:** The exact source requires `SortedSet` from its supporting library.
- **Persistent state:** Internal maps are intentionally mutated across API calls.
