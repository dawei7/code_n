# LFU Cache

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 460 |
| Difficulty | Hard |
| Topics | Hash Table, Linked List, Design, Doubly-Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/lfu-cache/) |

## Problem Description
### Goal
Implement a fixed-capacity key-value cache. A successful `get(key)` returns the value and increases that key's access frequency; a missing lookup returns `-1`. `put(key, value)` inserts a new key or updates an existing value, with an existing-key update also counting as use.

When inserting into a full cache, evict the key with the smallest frequency. If several keys tie, evict the least recently used among that frequency group. A newly inserted key starts at frequency one, and zero capacity stores nothing. Process all operations in average $O(1)$ time and return aligned results, using `None` for construction and puts.

### Function Contract
**Inputs**

- `operations`: method names beginning with `"LFUCache"`, followed by `"put"` and `"get"` calls
- `arguments`: the corresponding constructor capacity, key/value pairs, or lookup keys

**Return value**

- One trace entry per operation: `None` for construction and `put`, the stored value for a successful `get`, and `-1` for a missing key

### Examples
**Example 1**

- Input: `operations = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]`, `arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]`
- Output: `[None, None, None, 1, None, -1, 3, None, -1, 3, 4]`

**Example 2**

- Input: `operations = ["LFUCache", "put", "get"]`, `arguments = [[0], [1, 1], [1]]`
- Output: `[None, None, -1]`

**Example 3**

- Input: `operations = ["LFUCache", "put", "put", "put", "get"]`, `arguments = [[2], [1, 1], [2, 2], [1, 10], [1]]`
- Output: `[None, None, None, None, 10]`
