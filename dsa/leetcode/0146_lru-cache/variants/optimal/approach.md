## General
**The map and list answer different constant-time questions**

Maintain a hash map from each cached key to its unique node, plus a doubly linked list ordered from least to most recently used. The map locates a key in expected constant time; the first real list node identifies the eviction victim without a scan.

Permanent `least` and `most` sentinels surround all real nodes. `_remove` reconnects a known node's two neighbors, and `_append_most_recent` inserts a node immediately before `most`. Because both neighbors always exist, neither helper needs empty-list or endpoint branches.

**Every successful access moves exactly one key to the newest end**

On `get`, return `-1` without changing order when the key is absent. Otherwise unlink its mapped node, append it at the most-recent end, and return its value.

On `put`, remove the existing node when the key is already present, then install the new key-value node in both structures at the most-recent end. If this insertion makes the map exceed `capacity`, remove `least.next` and delete that same key from the map.

The map therefore contains exactly the real list nodes, each key occurs once, and list order always increases from least to most recent. Moving only the accessed key preserves every untouched key's relative age, so after overflow `least.next` is precisely the required eviction victim. Updating the map and list together prevents detached stale nodes from remaining discoverable.

## Complexity detail
Each `get` or `put` performs a constant number of expected-$O(1)$ hash operations and pointer rewires, so its expected time is $O(1)$. For $q$ app operations, total processing time and the required result list are $O(q)$. The cache retains at most `capacity` real nodes, giving $O(\textit{capacity})$ cache space beyond the app output.

## Alternatives and edge cases
- **Linear list of key-value pairs:** makes recency visible but lookup and movement can cost $O(\textit{capacity})$ per operation.
- **Hash map with timestamps only:** locates keys quickly but still needs an $O(\textit{capacity})$ scan to find the oldest timestamp.
- **Ordered-map library:** can satisfy the same bounds concisely, though the explicit map-plus-list design exposes the invariant directly.
- Capacity one must evict the former key on every distinct insertion.
- Replacing an existing key changes its value and recency without increasing the number of cached keys.
- A successful `get` changes the next eviction victim; a failed `get` leaves order untouched.
