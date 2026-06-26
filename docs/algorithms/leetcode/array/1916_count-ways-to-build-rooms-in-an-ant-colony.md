# Count Ways to Build Rooms in an Ant Colony

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1916 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Tree, Depth-First Search, Graph Theory, Topological Sort, Combinatorics |
| Official Link | [count-ways-to-build-rooms-in-an-ant-colony](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/) |

## Problem Description & Examples
### Goal
Rooms form a rooted tree where each room can be built only after its parent. Count the number of valid build orders.

### Function Contract
**Inputs**

- `prevRoom`: `prevRoom[i]` is the parent of room `i`, with room `0` as the root.

**Return value**

Return the number of valid construction orders modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `prevRoom = [-1,0,1]`
- Output: `1`

**Example 2**

- Input: `prevRoom = [-1,0,0,1,2]`
- Output: `6`

**Example 3**

- Input: `prevRoom = [-1,0,0]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Build the child tree and run DFS. For each subtree, combine child build orders by interleaving their sequences while preserving each child's internal valid order. If child subtree sizes are `s1, s2, ...`, multiply child ways by multinomial coefficients based on those sizes. Precompute factorials and inverse factorials for combinations modulo the prime.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
