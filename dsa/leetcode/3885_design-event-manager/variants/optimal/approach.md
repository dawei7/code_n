## General

**Maintain both direct lookup and ranking order**

The manager needs two different operations:

- find an active event by `eventId` to change its priority;
- find the globally highest-priority event, breaking ties by smallest ID.

A dictionary handles direct lookup but cannot efficiently return the ranked best event. An ordered collection handles ranking but needs the old key to update a particular event. The source keeps both views synchronized.

`self.d` maps every active `eventId` to its current priority.

`self.sl` is a `SortedList` containing one tuple

`(-priority, eventId)`

for every active event.

**Why the tuple order matches the requested ranking**

`SortedList` orders tuples lexicographically in ascending order.

Negating priority reverses its order: a larger original priority becomes a smaller negative number and appears earlier. For equal priorities, the first tuple fields tie, so the smaller `eventId` appears earlier.

Therefore `self.sl[0]` is always the active event with:

1. maximum priority;
2. minimum ID among that priority.

This encodes both ranking rules in the data structure's ordinary ascending order.

**Constructor establishes one synchronized entry per event**

For every initial pair `(eventId,priority)`, the constructor inserts `(-priority,eventId)` into the sorted list and records the priority in the dictionary.

Initial IDs are unique, so no key replaces another and every active event receives exactly one representation in each structure.

The key tuple is also unique among active events because event IDs are unique, even when priorities tie.

**Update removes the exact old rank before adding the new rank**

For `updatePriority(eventId,newPriority)`, the active-event guarantee ensures `eventId` exists in `self.d`.

The source reads `old_priority` from the dictionary, removes

`(-old_priority,eventId)`

from the sorted list, adds

`(-newPriority,eventId)`,

and updates the dictionary.

Removing the old tuple is essential. Leaving it behind would create a stale historical version that could later be polled incorrectly. This source uses eager deletion, not lazy validation.

If the new priority equals the old one, removal followed by reinsertion preserves the same logical state. It does extra logarithmic work but remains correct.

**Polling the highest event**

If the sorted list is empty, there are no active events and the method returns minus one.

Otherwise `self.sl.pop(0)` removes the first ranked tuple. Its second component is the desired event ID. The source removes that ID from `self.d` as well, so the event becomes inactive in both representations, then returns the ID.

The priority is not returned because the contract asks only for `eventId`.

**Representation invariant**

After construction and after every method call:

- dictionary keys are exactly the active event IDs;
- for every active ID `e` with dictionary priority `p`, `self.sl` contains exactly one tuple `(-p,e)`;
- `self.sl` contains no tuple for an inactive ID and no stale priority version; and
- its first tuple, when present, is the correct poll result.

Construction establishes the invariant. Update replaces one synchronized tuple and dictionary value. Poll deletes the same active event from both structures. Induction over the operation sequence proves every result.

**Trace the first example**

Initial keys are `(-7,5)`, `(-7,2)`, and `(-4,9)`. Sorted order places `(-7,2)` first because IDs break the priority tie, so the first poll returns two.

Updating event nine to priority seven removes `(-4,9)` and inserts `(-7,9)`. Remaining highest keys are `(-7,5)` and `(-7,9)`, so the next poll returns five, followed by nine.

**Manifest/source mismatch**

The manifest summary describes a current-priority map plus a lazily validated heap containing historical versions. That is a common solution, but it is not the protected implementation.

This source uses `SortedList` and eagerly removes the old tuple on every update. It stores no historical versions and needs no stale-entry loop during polling.

The distinction affects both explanation and space behavior.

**External dependency**

`SortedList` is not part of Python's built-in containers; it normally comes from the `sortedcontainers` package. The execution environment must import and provide it. Its balanced, block-based implementation supports ordered insertion, removal, and indexed popping efficiently.

## Complexity detail

Let `E` be the initial event count and `A` the current active count.

Adding the initial events one at a time costs `O(E\log E)` overall. A priority update performs one ordered removal and one ordered insertion, each approximately `O(\log A)`. A nonempty poll removes index zero in approximately `O(\log A)`. Dictionary operations are expected `O(1)`.

Across `Q` calls, total time is

$$
O((E+Q)\log(E+Q)),
$$

matching the manifest's aggregate bound.

The sorted list and dictionary each store exactly one entry per active event, so peak auxiliary storage is `O(E)` because this interface never adds new IDs after construction and polling only decreases activity. The manifest's `O(E+Q)` is a valid loose upper bound for a lazy heap with stale versions, but the exact eager source uses the tighter `O(E)` space.

## Alternatives and edge cases

- **Lazy heap plus dictionary:** Push every updated version and discard stale heap tops during polls. This matches the manifest summary and has simple updates, but stale entries can grow storage to `O(E+Q)`.
- **Balanced search tree:** Store `(-priority,id)` keys with direct deletion. This is the abstract structure implemented by the source's ordered collection.
- **Sort all active events on every poll:** Simple but can take `O(A\log A)` per poll.
- **Scan the dictionary on every poll:** Uses no ordered structure but takes `O(A)` per poll.
- **Priority tie:** Negative priorities tie, so ascending tuple order chooses the smaller ID.
- **Update to the same priority:** Eager remove-and-add is logically neutral and preserves one entry.
- **Poll empty manager:** Returns minus one without touching the dictionary.
- **Poll removes activity:** A later update for that ID is excluded by the contract's active-ID guarantee.
- **Large priorities:** Python negation is exact and safely reverses order.
- **Unique IDs:** Required for dictionary identity and tuple uniqueness.
- **No stale keys:** Exact old-key removal is the core difference from a lazy heap.
- **Dependency availability:** Without `sortedcontainers.SortedList`, this exact source cannot run and needs another ordered structure.
- **Output protocol:** Constructor and updates conceptually yield null in the design harness; only polls return integers.
