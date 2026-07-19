## General
**Two data structures answer two independent constant-time questions**

Use a hash map `key -> node` for expected constant-time location. Store the same real nodes in a doubly linked list ordered from least recently used to most recently used. The map answers “where is this key?”, while the list answers “which key is oldest?” without scanning.

**Sentinels make removal and insertion uniform**

Dummy `least` and `most` nodes remain permanently linked around all real entries. Removing a known node always reconnects `node.prev.next` and `node.next.prev`; appending most-recent always inserts immediately before `most`. No operation needs separate empty-list, head, or tail branches.

**`get` and `put` both count as recent use**

For successful `get`, unlink the found node and append it at the most-recent end before returning its value. For `put` on an existing key, update or replace its node and make it most recent without increasing cache size. For a new key, append once; if size now exceeds capacity, remove `least.next` from both list and map.

A missing `get` returns `-1` and changes no recency.

**Map membership and list membership must change atomically**

The map contains exactly the real list nodes, every key appears once, and left-to-right list order is increasing recency. Every helper unlink/append preserves bidirectional links. Eviction must delete the same node from the map, or future lookup would return a detached stale entry.

**Map identity and list order make eviction exact**

The map locates the unique node for each stored key, while the doubly linked list orders those nodes from least to most recent. Every successful access or write moves exactly that node to the newest end; untouched nodes retain their relative age.

When capacity is exceeded, the first real list node is therefore precisely the least recently used key. Removing that same node from both list and map preserves identity synchronization and makes all future lookups and evictions correct.

## Complexity detail
Hash lookup, unlinking a known node, appending it, and removing the oldest node are all expected $O(1)$. At most `capacity` real nodes are stored, so space is $O(capacity)$.

## Alternatives and edge cases
- **List of key-value pairs:** makes recency explicit but lookup or movement costs $O(capacity)$.
- **Hash map with timestamps:** gives quick lookup but finding the oldest timestamp costs $O(capacity)$ unless another ordered structure is added.
- **Ordered-map library:** can satisfy the complexity concisely, but implementing map plus linked list demonstrates the required invariant directly.
- Capacity may be one. Updating an existing key changes its value and recency without increasing size.
- A successful `get` can change the next eviction victim; a failed `get` cannot.
