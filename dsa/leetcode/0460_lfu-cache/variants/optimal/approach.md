## General

An LFU cache has two priorities. It first evicts the key with the smallest use frequency. If several keys have that frequency, it evicts the least recently used among them. Supporting both rules in average $O(1)$ time requires more than one ordering structure: a hash map provides direct access by key, while a separate recency list is maintained for every frequency.

The exact solution uses four pieces of state:

- `map` associates each cached key with its `Node` object.
- Every node stores `key`, `value`, its current `freq`, and doubly linked `prev` and `next` pointers.
- `freq_map[f]` is a doubly linked list containing exactly the active nodes used `f` times.
- `min_freq` is the smallest frequency among active cache nodes and identifies the only bucket eligible for eviction.

**Frequency buckets also maintain recency**

Each `DoublyLinkedList` has dummy `head` and `tail` sentinels. Real nodes lie between them. `add_first(node)` inserts immediately after `head`, making the node the most recently used member of its frequency bucket. The node just before `tail` is therefore the least recently used member.

The sentinels remove boundary special cases. Inserting into an empty list and removing its sole real node use the same four pointer updates as operations on a longer list. `is_empty()` simply checks whether `head.next` is `tail`.

Given a node reference, `remove(node)` reconnects its predecessor directly to its successor. It never searches the list, so removal is $O(1)$. `remove_last()` removes `tail.prev`, giving the LRU node of that frequency in constant time.

**What counts as a use**

A successful `get(key)` is a use. Updating an existing key through `put(key, value)` is also a use. A newly inserted key starts at frequency one because its insertion counts as its first use.

Whenever an existing node is used, `incr_freq(node)` performs the complete transition:

1. Save its old frequency `freq` and remove it from `freq_map[freq]`.
2. If that bucket becomes empty, remove the bucket entry. If it was also `min_freq`, increment `min_freq`.
3. Increment the node's own frequency.
4. Insert the node at the front of its new frequency list, making it most recent among nodes now tied at that frequency.

Incrementing `min_freq` by exactly one is safe in this situation. The node being moved immediately creates a nonempty bucket at `freq + 1`. If no nodes remain at the old minimum, the new minimum cannot skip above that bucket.

**Successful and unsuccessful `get` operations**

If capacity is zero or the key is absent, `get` returns `-1` and changes no frequency or recency state. Although the source constraints use positive capacity, the explicit zero check makes the class robust to zero.

For a present key, direct map lookup finds its node in expected constant time. The node moves to the next frequency bucket through `incr_freq`, and its stored value is returned. Because it is inserted at the front of the new bucket, this access is also recorded as the most recent event among keys with that new frequency.

**Updating an existing key**

When `put` finds the key already cached, it replaces `node.value`, then calls `incr_freq(node)`. Cache size does not change and no eviction occurs. This matches the contract's rule that a `put` on an existing key increments its use counter.

**Inserting and evicting**

For a new key, eviction is needed only when `len(map) == capacity`. `min_freq` identifies the least frequency, and `freq_map[min_freq].remove_last()` selects the least recently used node among all keys tied at that frequency. Removing that key from `map` completes eviction.

The new `Node` begins with `freq = 1`. `add_node` inserts it at the front of frequency bucket one, the key map receives its direct reference, and `min_freq` is reset to one. Resetting is necessary because a newly inserted active key always establishes frequency one, regardless of how large the previous minimum was.

**Trace the main example**

With capacity two, inserting keys `1` and `2` puts both in frequency bucket one. Key `2` is more recent because it was inserted last, so the bucket runs from most recent `2` to least recent `1`.

`get(1)` removes key `1` from bucket one and inserts it into bucket two. Key `2` is now the sole minimum-frequency entry. Inserting key `3` evicts key `2`, not key `1`, because frequency one loses before frequency two.

After `get(3)`, keys `1` and `3` both have frequency two. Key `3` entered that bucket most recently, so key `1` is at the tail side. Inserting key `4` sees a frequency tie and evicts key `1`, exactly applying the LRU tiebreaker.

**Why eviction always chooses the required key**

Every use removes a node from its exact old-frequency list and inserts it into its exact new-frequency list, so bucket membership agrees with use counters. `min_freq` changes only when its bucket empties or a new frequency-one node appears, keeping it equal to the smallest active counter. Within each bucket, every use places a node at the front, so order from front to back is newest to oldest. The tail-side node of the minimum bucket is therefore precisely the globally LFU key and, among ties, the LRU key.

## Complexity detail

Hash-map lookup, insertion, and deletion are expected $O(1)$. Doubly linked insertion and removal change a fixed number of pointers and are worst-case $O(1)$. `min_freq` avoids searching frequency buckets. Thus each `get` and `put` takes expected $O(1)$ time, and a trace of $m$ operations takes expected $O(m)$ time, matching the manifest's time notation.

There are at most `capacity` active data nodes. Their key-map entries and active frequency memberships use $O(\texttt{capacity})$ space. Each nonempty frequency bucket has two sentinels, and there can be no more nonempty buckets than active nodes.

The exact eviction path has a subtle storage issue: after `remove_last()`, it does not delete that frequency-list entry when the list becomes empty. The next insertion resets `min_freq` to one, so stale empty buckets do not affect eviction correctness. However, repeated evictions from different high frequencies can leave many empty `DoublyLinkedList` objects in `freq_map`. Consequently, the exact source's worst-case total storage can grow to $O(m+\texttt{capacity})$, rather than the manifest's strict $O(\texttt{capacity})$.

To restore the intended bound, after eviction check `ls.is_empty()` and remove `freq_map[min_freq]` before inserting the new node. Then only active frequency buckets remain, and total auxiliary space is $O(\texttt{capacity})$.

## Alternatives and edge cases

- **Frequency heap:** Store `(frequency, time, key)` entries in a min-heap. Eviction is logarithmic and stale heap entries require lazy cleanup, so it does not meet average $O(1)$ operations.
- **One global linked list:** LRU order is easy, but moving a node to the correct place after a frequency increase requires searching or another ordering structure.
- **Ordered map per frequency:** A language-provided insertion-ordered map can replace the custom linked list if it supports arbitrary deletion and removal of the oldest key in constant time.
- **Delete empty eviction buckets:** Removing the bucket after its last node is evicted prevents stale-list accumulation and makes the advertised capacity-bound space exact.
- **Capacity zero:** `get` returns `-1` and `put` does nothing. The supplied constraints are positive, but the guards are coherent.
- **Missing `get`:** It returns `-1` without creating a node or changing recency.
- **Existing-key `put`:** Value changes and frequency increments; it is not treated as a new frequency-one insertion.
- **Frequency tie:** `remove_last` selects the least recently used node within `min_freq`.
- **Single-slot cache:** Every new distinct key evicts the current one. Successful accesses still raise its frequency until replacement resets the minimum to one.
- **Sentinel safety:** `remove_last` assumes a nonempty active minimum bucket. Cache fullness and correct `min_freq` ensure that for valid state.
- **`defaultdict(Node)` for `map`:** The node factory requires constructor arguments, but correct code checks membership before indexing a missing key, so the factory is never invoked. A plain dictionary would communicate this intent more clearly.
