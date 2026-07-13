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

### Required Complexity

- **Time:** $O(q)$
- **Space:** $O(U + B)$

<details>
<summary>Approach</summary>

#### General

**Hash each key to one collision chain**

Allocate `B` list buckets and select `key % B`. Store each mapping as a two-item `[key, value]` entry in that bucket, allowing different keys with the same hash to coexist.

**Make put update or append**

Scan the chosen bucket for the key. If found, replace that entry's value and return; otherwise append a new mapping. This maintains exactly one current value per stored key.

**Share the same lookup for get and remove**

Getting returns the matching entry's value or `-1` after the bucket is exhausted. Removing deletes the matching entry if present and otherwise changes nothing.

**Why bucket-local search is complete**

The deterministic modulo function always maps the same key to the same bucket, so its mapping cannot legally reside elsewhere. The uniqueness rule within that bucket makes a found entry authoritative, and exhausting the chain proves absence.

#### Complexity detail

With well-distributed keys, a bucket has expected constant length, so `q` operations take expected $O(q)$ time. The bucket headers and `U` stored mappings use $O(U + B)$ space. If adversarial keys all collide, one operation can take $O(U)$.

#### Alternatives and edge cases

- **Direct-address array:** store a value at every possible key index and reserve `-1` for absence; operations are worst-case $O(1)$ but memory covers the full domain.
- **Resizable chaining table:** rehash into more buckets as the load factor grows; it controls expected chain length for unbounded use.
- **Flat association list:** keep all key/value pairs together and scan for every operation; it is correct but can take $O(q^2)$ total time.
- Putting an existing key changes its value without creating another entry.
- Values may be zero, so absence must use the specified `-1` result.
- Removing an absent key leaves all mappings unchanged.
- Colliding keys must retain independent values and removal behavior.

</details>
