# LRU Cache

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 146 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Design, Doubly-Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lru-cache/) |

## Problem Description
### Goal
Implement a key-value cache that stores at most a fixed positive `capacity` of entries. `get(key)` returns the stored value when the key exists and `-1` otherwise. `put(key, value)` inserts a new entry or replaces an existing value without increasing the number of entries for that key.

Successful `get` calls and all `put` calls make their key the most recently used. When inserting a missing key into a full cache, first evict the key whose most recent successful access or update is oldest. Process the supplied operation sequence in order and return aligned results, using `None` for construction and updates. Both cache operations must meet the required constant average-time behavior.

### Function Contract
**Inputs**

- `operations`: method names beginning with `LRUCache`, followed by `get` and `put` calls
- `arguments`: one argument list for each operation; the constructor receives capacity, `get` receives a key, and `put` receives a key and value

**Return value**

A list aligned with the operations: `None` for construction and `put`, and the stored value or `-1` for each `get`.

### Examples
**Example 1**

- Input: `operations = [LRUCache, put, put, get, put, get]`, `arguments = [[2],[1,1],[2,2],[1],[3,3],[2]]`
- Output: `[null,null,null,1,null,-1]`

**Example 2**

- Input: capacity `1`, then `put(1,1)`, `put(2,2)`, `get(1)`, `get(2)`
- Output: `[null,null,null,-1,2]`

**Example 3**

- Input: capacity `2`, then access key `1` before inserting key `3`
- Output: key `2` is evicted because key `1` became most recently used

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(capacity)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Hash lookup, unlinking a known node, appending it, and removing the oldest node are all expected $O(1)$. At most `capacity` real nodes are stored, so space is $O(capacity)$.

#### Alternatives and edge cases

- **List of key-value pairs:** makes recency explicit but lookup or movement costs $O(capacity)$.
- **Hash map with timestamps:** gives quick lookup but finding the oldest timestamp costs $O(capacity)$ unless another ordered structure is added.
- **Ordered-map library:** can satisfy the complexity concisely, but implementing map plus linked list demonstrates the required invariant directly.
- Capacity may be one. Updating an existing key changes its value and recency without increasing size.
- A successful `get` can change the next eviction victim; a failed `get` cannot.

</details>
