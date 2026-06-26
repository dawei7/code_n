# Operations on Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1993 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Design |
| Official Link | [operations-on-tree](https://leetcode.com/problems/operations-on-tree/) |

## Problem Description & Examples
### Goal
Design a tree locker that supports locking, unlocking, and upgrading nodes under ancestor/descendant rules.

### Function Contract
**Inputs**

- `parent`: parent array for the tree.
- Operations: `lock(num, user)`, `unlock(num, user)`, and `upgrade(num, user)`.

**Return value**

`lock` and `unlock` return whether they changed the node. `upgrade` locks the node and unlocks locked descendants only when the upgrade rules are satisfied.

### Examples
**Example 1**

- Input: `["LockingTree","lock","unlock","unlock","lock","upgrade","lock"], [[[-1,0,0,1,1,2,2]],[2,2],[2,3],[2,2],[4,5],[0,1],[0,1]]`
- Output: `[null,true,false,true,true,true,false]`

**Example 2**

- Input: `parent = [-1,0,0], operations = lock(1,7), upgrade(0,9)`
- Output: `[true,true]`

**Example 3**

- Input: `parent = [-1,0], operations = upgrade(0,1), lock(0,1), unlock(0,2)`
- Output: `[false,true,false]`

---

## Underlying Base Algorithm(s)
Store the locking user per node and build child adjacency from `parent`. `lock` and `unlock` are direct checks. `upgrade` verifies the target is unlocked, no ancestor is locked, and at least one descendant is locked; then DFS through descendants to clear locks before locking the target.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` per `upgrade`, `O(1)` to lock/unlock plus ancestor walk if needed.
- **Space Complexity**: `O(n)`
