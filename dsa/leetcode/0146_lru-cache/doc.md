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
