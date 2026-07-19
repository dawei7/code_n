# Map Sum Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 677 |
| Difficulty | Medium |
| Topics | Hash Table, String, Design, Trie |
| Official Link | [LeetCode](https://leetcode.com/problems/map-sum-pairs/) |

## Problem Description
### Goal
Design a `MapSum` data structure that maps string keys to integer values. `insert(key, val)` adds a new key-value pair or overrides the old value when the key already exists.

The operation `sum(prefix)` returns the sum of the current values of all stored keys that start with the requested prefix. A replaced key contributes only its new value, not both versions, and keys outside the prefix contribute nothing. Repeated queries do not modify the map.

### Function Contract
**Inputs**

- `operations`: constructor, `insert`, and `sum` calls in execution order
- `arguments`: paired arguments; `insert` receives a lowercase key and value, while `sum` receives a lowercase prefix

**Return value**

- A result list aligned with the operations: `null` for construction and insertion, and the matching prefix total for every `sum` call

### Examples
**Example 1**

- Input: `insert("apple", 3); sum("ap")`
- Output: `3`

**Example 2**

- Input: `insert("apple", 3); insert("app", 2); sum("ap")`
- Output: `5`

**Example 3**

- Input: `insert("apple", 3); insert("apple", 2); sum("ap")`
- Output: `2`
