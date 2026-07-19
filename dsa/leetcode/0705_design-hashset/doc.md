# Design HashSet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 705 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Linked List, Design, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/design-hashset/) |

## Problem Description
### Goal
Design `MyHashSet` without using a built-in hash-table library. The data structure begins empty and stores integer keys without associated values.

Implement `add(key)` to insert a key, `contains(key)` to report whether it currently exists, and `remove(key)` to delete it. Adding an already stored key leaves one logical copy, while removing an absent key does nothing. State persists across calls, and membership reflects every earlier successful addition and removal.

### Function Contract
**Inputs**

- `operations`: ordered `[name, key]` pairs, where `name` is `"add"`, `"remove"`, or `"contains"`

**Return value**

- A list of Boolean results, one for each `contains` operation in input order

### Examples
**Example 1**

- Input: `operations = [["add",1],["contains",1],["remove",1],["contains",1]]`
- Output: `[true,false]`

**Example 2**

- Input: `operations = [["contains",13],["remove",2],["contains",17],["remove",13]]`
- Output: `[false,false]`

**Example 3**

- Input: `operations = [["add",5],["add",9],["contains",5],["contains",16]]`
- Output: `[true,false]`
