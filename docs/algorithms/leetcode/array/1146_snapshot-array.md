# Snapshot Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1146 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Design |
| Official Link | [snapshot-array](https://leetcode.com/problems/snapshot-array/) |

## Problem Description & Examples
### Goal
Design an array that supports point updates, immutable snapshots, and historical reads by snapshot id.

### Function Contract
**Inputs**

- Constructor receives `length`.
- `set(index, val)` writes the current value at `index`.
- `snap()` records the current array state and returns its id.
- `get(index, snap_id)` reads the value at `index` as it was at the given snapshot.

**Return value**

Methods return `None`, a snapshot id, or a historical value according to the method contract.

### Examples
**Example 1**

- Input: `SnapshotArray(3); set(0,5); snap(); set(0,6); get(0,0)`
- Output: `5`

**Example 2**

- Input: `SnapshotArray(1); snap(); snap(); get(0,1)`
- Output: `0`

**Example 3**

- Input: `SnapshotArray(2); set(1,7); set(1,8); snap(); get(1,0)`
- Output: `8`

---

## Underlying Base Algorithm(s)
Sparse version history with binary search.

---

## Complexity Analysis
- **Time Complexity**: `set` is `O(1)`, `snap` is `O(1)`, and `get` is `O(log u)` for `u` updates at that index.
- **Space Complexity**: `O(length + number_of_sets)`
