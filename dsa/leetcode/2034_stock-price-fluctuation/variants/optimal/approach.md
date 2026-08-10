## General

**Maintain two synchronized views of the records**

The class must answer questions by timestamp and by price. One structure is not enough to make every operation efficient.

`self.d` is a dictionary mapping each timestamp to its current corrected price. It is authoritative for corrections and for looking up the price at the latest timestamp.

`self.ls` is a `SortedList` containing one price for every currently recorded timestamp. It is a multiset: equal prices may appear several times. Its first and last entries provide the current minimum and maximum prices.

`self.last` stores the greatest timestamp ever recorded. Together, these three pieces represent the same logical record set from complementary directions.

**Insert a previously unseen timestamp**

When `timestamp` is absent from the dictionary, `update` adds `timestamp -> price` to `d` and inserts `price` into the sorted multiset.

It then sets `last = max(last, timestamp)`. An out-of-order update with a smaller timestamp leaves the latest timestamp unchanged; an update with a larger timestamp makes it the new latest.

After these actions, the dictionary has one additional record and the sorted list has exactly one corresponding additional price.

**Correct an existing timestamp without leaving a stale price**

If the timestamp already exists, its old price must stop affecting minimum and maximum queries. The source retrieves `d[timestamp]` and removes one occurrence of that value from `ls` before storing the replacement.

Removing exactly one occurrence matters. Two different timestamps may legitimately share the same price. Correcting one of them must not remove both copies, because the other timestamp's price is still current.

After removal, the dictionary entry is overwritten and the new price is added to `ls`. The number of dictionary entries and multiset entries remains equal.

**Why the latest timestamp never needs to decrease**

Records can be corrected but not deleted. Once a timestamp has appeared, it remains present in `d` after every correction. Therefore the greatest recorded timestamp can only stay the same or increase as updates arrive.

The `max` assignment is sufficient; there is no need to recompute the maximum dictionary key after a correction. If the latest timestamp itself is corrected, `last` remains that timestamp and `d[last]` immediately exposes its new price.

**Answer `current`**

`current` returns `self.d[self.last]`. The dictionary lookup obtains the current corrected price for the greatest recorded timestamp.

This must not be confused with the most recently received update. A late-arriving correction for timestamp one does not make timestamp one the “latest” record when timestamp ten is already known. Latest is defined by timestamp value, not arrival order.

**Answer `maximum` and `minimum`**

Because `ls` is kept sorted, `ls[-1]` is its greatest price and `ls[0]` is its smallest price.

The contract guarantees that these methods are called only after at least one update, so both endpoints exist. Corrections are already reflected because the old occurrence was removed before the new one was added.

**Trace the example**

After updates `(1,10)` and `(2,5)`, the dictionary is logically `{1:10, 2:5}`, the sorted prices are `[5,10]`, and `last=2`. Thus `current` returns five and `maximum` returns ten.

Correcting timestamp one to price three removes one occurrence of ten, writes `d[1]=3`, and inserts three. The sorted prices become `[3,5]`. Timestamp two remains latest, so `current` would still be five, while `maximum` now also returns five.

Updating timestamp four to price two adds a new record, changes `last` to four, and produces sorted prices `[2,3,5]`. The minimum is two and the current price is also two.

**The representation invariant**

After every completed `update`:

- `d` contains exactly one current price for every recorded timestamp;
- `ls` contains exactly the multiset of all values in `d`, including duplicate multiplicities;
- `last` is the maximum key in `d`.

The constructor establishes the empty form of this invariant. A new-timestamp update adds matching entries to both structures and adjusts the maximum key. A correction replaces one dictionary value and the corresponding one multiset occurrence without changing keys. Induction proves the invariant after any update sequence.

Given the invariant, all three query methods are immediate: `current` reads the value at the maximum key, and the sorted endpoints are the extrema of all current dictionary values.

**Why a multiset is required**

A plain set of prices would collapse duplicates. Suppose timestamps one and two both have price five. Correcting timestamp one to seven would remove five from a plain set, incorrectly suggesting no current record has price five. `SortedList` preserves two copies and removes only one, leaving the other intact.

The dictionary alone handles correction lookup but would require scanning all prices for every minimum or maximum query. The sorted multiset avoids that repeated linear work.

## Complexity detail

Let $Q$ be the number of distinct recorded timestamps. Dictionary membership, lookup, and assignment are expected $O(1)$. `SortedList.add` and `SortedList.remove` take $O(\log Q)$ amortized time in the intended sorted-container implementation, so `update` is $O(\log Q)$.

`current` uses one dictionary lookup and is expected $O(1)$. Accessing a sorted endpoint is constant or logarithmic depending on the container's indexing details; in either case `maximum` and `minimum` are within the manifest's $O(\log Q)$ per-operation upper bound.

The dictionary and sorted multiset each store one item per distinct timestamp, so space is $O(Q)$. Corrections do not increase $Q$.

## Alternatives and edge cases

- **Dictionary plus two heaps:** Push corrected prices lazily and discard stale heap tops during queries; updates are simple but heaps may retain obsolete entries.
- **Balanced map from price to frequency:** Maintain counts at sorted price keys; it provides the same multiset behavior.
- **Scan dictionary values:** Makes updates cheap but every minimum and maximum query costs $O(Q)$.
- **Repeated timestamp:** Remove its old price once before adding the corrected price.
- **Duplicate prices at different timestamps:** The multiset retains separate occurrences.
- **Correction to the same price:** One occurrence is removed and re-added, leaving the logical state unchanged.
- **Out-of-order older update:** It does not change `last`.
- **New greatest timestamp:** It becomes `last` even if its price is not an extreme.
- **Correction at the latest timestamp:** `current` immediately returns the replacement price.
- **Current versus last arrival:** `current` follows the largest timestamp, not call order.
- **Single record:** Its price is simultaneously current, minimum, and maximum.
- **Query before update:** Excluded by the contract, so empty-endpoint handling is unnecessary.
- **No deletion operation:** This is why `last` never needs to move backward.
