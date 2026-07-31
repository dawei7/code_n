## Description

Design an `LRUCache` class that stores key-value pairs up to a positive, fixed `capacity`. The cache must expose these operations:

- `LRUCache(int capacity)` creates an empty cache with the given capacity.
- `get(key)` returns the value associated with `key`, or `-1` when that key is absent. A successful lookup makes the key the most recently used entry.
- `put(key, value)` updates an existing key or inserts a new key-value pair. The written key becomes the most recently used entry. If an insertion would exceed the capacity, remove the least recently used key first.

Both `get` and `put` must run in $O(1)$ average time.
