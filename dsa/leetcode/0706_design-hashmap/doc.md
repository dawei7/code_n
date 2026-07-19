# Design HashMap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 706 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Linked List, Design, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/design-hashmap/) |

## Problem Description
### Goal
Design `MyHashMap` without using a built-in hash-table library. The map begins empty and associates integer keys with integer values.

Implement `put(key, value)` to insert a mapping or update the value of an existing key, `get(key)` to return its current value or `-1` when no mapping exists, and `remove(key)` to delete the mapping if present. Removing an absent key has no effect, and state persists across all operation calls.

### Function Contract
**Inputs**

- `operations`: ordered `["put", key, value]`, `["get", key]`, or `["remove", key]` records

**Return value**

- A list of integer results, one for each `get` operation in input order

### Examples
**Example 1**

- Input: `operations = [["put",1,10],["get",1],["get",2]]`
- Output: `[10,-1]`

**Example 2**

- Input: `operations = [["put",2,20],["put",2,30],["get",2]]`
- Output: `[30]`

**Example 3**

- Input: `operations = [["put",1,5],["remove",1],["get",1]]`
- Output: `[-1]`
