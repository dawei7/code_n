# Jump Game IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1345 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Breadth-First Search |
| Official Link | [jump-game-iv](https://leetcode.com/problems/jump-game-iv/) |

## Problem Description & Examples
### Goal
Starting at index `0`, reach the last index in the fewest jumps. From index `i`, you may move to `i - 1`, `i + 1`, or any other index with the same value.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The minimum number of jumps needed to reach index `len(arr) - 1`.

### Examples
**Example 1**

- Input: `arr = [100,-23,-23,404,100,23,23,23,3,404]`
- Output: `3`

**Example 2**

- Input: `arr = [7]`
- Output: `0`

**Example 3**

- Input: `arr = [7,6,9,6,9,6,9,7]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Breadth-first search with value buckets.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
