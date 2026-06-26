# Queries on a Permutation With Key

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1409 |
| Difficulty | Medium |
| Topics | Array, Binary Indexed Tree, Simulation |
| Official Link | [queries-on-a-permutation-with-key](https://leetcode.com/problems/queries-on-a-permutation-with-key/) |

## Problem Description & Examples
### Goal
Maintain a permutation of numbers `1..m`. For each query value, report its current zero-based index, then move that value to the front of the permutation.

### Function Contract
**Inputs**

- `queries`: the values to look up and move.
- `m`: the largest value in the initial permutation `1..m`.

**Return value**

A list of indices, one for each query before it is moved to the front.

### Examples
**Example 1**

- Input: `queries = [3,1,2,1], m = 5`
- Output: `[2,1,2,1]`

**Example 2**

- Input: `queries = [4,1,2,2], m = 4`
- Output: `[3,1,2,0]`

**Example 3**

- Input: `queries = [7,5,5,8,3], m = 8`
- Output: `[6,5,0,7,5]`

---

## Underlying Base Algorithm(s)
Simulation or indexed order statistics. The direct solution keeps a list and moves queried values to the front; an optimized solution uses a Fenwick tree with reserved front positions to support index queries and moves in logarithmic time.

---

## Complexity Analysis
- **Time Complexity**: `O(qm)` for direct simulation, or `O((q + m) log(q + m))` with a Fenwick tree.
- **Space Complexity**: `O(m)` for simulation, or `O(q + m)` for the Fenwick tree approach.
