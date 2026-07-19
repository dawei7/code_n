## General
**Separate direct lookup from eviction order**

Map every key directly to its value and current frequency. Separately map each frequency to an insertion-ordered set of keys; within one frequency bucket, oldest means least recently used. Track the smallest nonempty frequency in `minimum_frequency`, so eviction never searches across keys or frequencies.

**Promote every successful access**

A successful `get` and an update to an existing key both count as uses. Remove the key from its current frequency bucket, delete the bucket if it becomes empty, increment the frequency, and append the key to the new bucket as most recent. If the emptied bucket was the minimum, the minimum rises by exactly one because the promoted key created or joined that next bucket.

**Evict the oldest key at the minimum frequency**

When a new insertion would exceed capacity, remove the first key from the `minimum_frequency` bucket. All keys in higher buckets have been used more often, and insertion order inside the selected bucket identifies the least recently used tie. Insert the new key at frequency one and reset the minimum to one.

**Why the bookkeeping stays sufficient**

Every resident key appears once in the direct map and once in exactly one frequency bucket. Promotion preserves that correspondence; eviction removes both entries. These facts make direct access, recency updates, and victim selection local constant-time operations without a stale candidate.

## Complexity detail
Ordered-map lookup, deletion, append, and removal of the oldest entry are average $O(1)$, so `m` traced operations take $O(m)$ total time. Each resident key is stored in the direct map and one frequency bucket, using $O(capacity)$ space.

## Alternatives and edge cases
- **Custom doubly linked lists per frequency:** provides the same $O(1)$ guarantees in languages without insertion-ordered maps, but requires explicit node unlinking.
- **Lazy priority queue:** can encode frequency and time, but updates add stale entries and cost $O(\log capacity)$ per operation.
- **Scan all entries on eviction:** is simple and correct but makes each full-cache insertion $O(capacity)$.
- **Zero capacity:** every `put` is ignored and every `get` misses.
- **Updating a key:** changes its value and increments both frequency and recency; it is not a fresh frequency-one insertion.
- **Frequency tie:** evict the least recently used key within that exact frequency.
- **Missing `get`:** returns `-1` and changes no frequency or recency state.
