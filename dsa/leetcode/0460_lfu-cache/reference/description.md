## Description

Design and implement a **Least Frequently Used (LFU) cache** with these operations:

- `LFUCache(int capacity)` creates a cache with the given maximum number of keys.
- `get(int key)` returns the stored value when the key exists, or `-1` otherwise.
- `put(int key, int value)` updates an existing key or inserts a new key-value pair.

Every resident key has a use counter. A new key starts with frequency `1` because its insertion is a use; a successful `get` or an update through `put` increments the key's counter.

Before inserting a new key into a full cache, remove the key with the smallest use counter. When several keys share that minimum frequency, evict the least recently used one among them.

Both `get` and `put` must run in average $O(1)$ time.
