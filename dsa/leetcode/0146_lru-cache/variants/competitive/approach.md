## General

**Let ordered-map position represent recency**

Python’s `OrderedDict` combines key-value lookup with a maintained key order. The competitive source interprets that order as:

- first item: least recently used;
- last item: most recently used.

Every successful access or update moves its key to the last position. Every new insertion also appears last. When capacity is full, the first item is evicted.

The class stores only `cache` and `capacity`; the library owns the linked-order bookkeeping internally.

**One helper handles insertion, update, and promotion**

`__update(key, val)` checks whether the key already exists. If it does, the old entry is deleted. The helper then assigns `self.cache[key] = val`.

In an `OrderedDict`, assigning a brand-new key places it at the end. Deleting an existing key first makes the subsequent assignment act like a new insertion, so it also moves that key to the end.

This helper therefore guarantees two postconditions:

- the stored value for `key` equals `val`;
- `key` is the most recently used entry.

The double underscore triggers Python name mangling, making the helper an implementation detail named similarly to `_LRUCache__update`; it does not affect algorithmic behavior.

**Read without forgetting to refresh recency**

`get` first checks membership. An absent key returns `-1` without changing order.

For a present key, it saves the value, calls `__update(key, val)`, and returns the saved value. The helper’s delete-and-reinsert action moves the key from wherever it was to the most-recent end.

It would be incorrect to return `self.cache[key]` without promotion: then frequently read entries could remain at the oldest end and be evicted despite recent use.

**Evict only for a new key at full capacity**

`put` tests:

`key not in self.cache and len(self.cache) == self.capacity`

Only that situation increases the number of stored keys beyond capacity. The source removes the oldest item with `popitem(last=False)`. `last=False` selects the first ordered entry, which is the least recently used under the maintained invariant.

After any necessary eviction, `__update(key, val)` stores the value at the most-recent end.

If the key already exists, no eviction occurs even when the cache is full because updating does not increase its size. The helper merely changes its value and recency.

The positive-capacity guarantee ensures `popitem` is never called on an empty cache in a valid construction.

**Trace the sample ordering**

With capacity two:

- `put(1, 1)` gives order `[1]`;
- `put(2, 2)` gives `[1, 2]`, with one least recent;
- `get(1)` returns one and changes order to `[2, 1]`;
- `put(3, 3)` removes first key two, then gives `[1, 3]`;
- a miss on key two leaves that order unchanged;
- `put(4, 4)` removes key one and gives `[3, 4]`.

Subsequent gets return three and four, promoting each as they occur.

**Why the recency invariant persists**

Initially the ordered map is empty. A new operation involving a stored key removes its old position and reinserts it last, accurately recording the newest use. A new key also enters last. No other keys change relative order.

When eviction is necessary, removing the first item deletes exactly the entry whose last use happened earliest. Therefore, after every public operation, iteration order remains least recent through most recent.

The later `LRUCache2` class in the file manually implements the map-plus-linked-list design. It is not the selected class named `LRUCache`; the primary approach here is the built-in ordered map.

## Complexity detail

Let $C$ be capacity.

`OrderedDict` membership, indexing, deletion, insertion, and endpoint `popitem` are expected $O(1)$ operations. Each public method performs only a fixed number of them, so `get` and `put` have expected $O(1)$ time per call.

The map contains at most $C$ entries. Its values and internal ordering links therefore use $O(C)$ space, matching the manifest.

Deleting and reinserting an existing key may do more constant-factor work than a direct `move_to_end`, but it does not change the asymptotic bound.

## Alternatives and edge cases

- **Explicit hash map plus doubly linked list:** It demonstrates the required mechanism directly and avoids dependence on `OrderedDict`, at the cost of more pointer code.
- **Use `move_to_end`:** Update the value and call the built-in promotion method. It expresses intent more directly than delete-and-reinsert.
- **Plain dictionary order alone:** Modern dictionaries retain insertion order, but updating an existing value does not move its key; explicit deletion/reinsertion would still be required.
- **Capacity one:** A new distinct key pops the sole oldest item before insertion.
- **Existing key in a full cache:** It is updated and promoted without evicting an unrelated key.
- **Missed `get`:** A missing key does not become recent and does not alter membership.
- **Stored zero:** It is returned normally; only `-1` signals absence under the value constraints.
- **Positive capacity:** The code assumes the contractual lower bound of one when calling `popitem` on a full cache.
- **Least-recent endpoint:** `last=False` is essential. The default would pop the newest entry and implement the wrong replacement policy.
- **Average-time qualification:** Hash-based ordered maps have expected constant operations, not an absolute worst-case guarantee against pathological collisions.
- **Thread safety:** The compound check, eviction, and update are not synchronized for concurrent callers.
