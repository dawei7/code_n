# Jump Game III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1306 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search |
| Official Link | [jump-game-iii](https://leetcode.com/problems/jump-game-iii/) |

## Problem Description & Examples
### Goal
Starting at index `start`, repeatedly jump left or right by the value at the current index. Decide whether some sequence of jumps can reach an index whose value is `0`.

### Function Contract
**Inputs**

- `arr`: non-negative integer array.
- `start`: starting index.

**Return value**

`true` if a zero-valued index is reachable, otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 5`
- Output: `true`

**Example 2**

- Input: `arr = [4,2,3,0,3,1,2]`, `start = 0`
- Output: `true`

**Example 3**

- Input: `arr = [3,0,2,1,2]`, `start = 2`
- Output: `false`

---

## Underlying Base Algorithm(s)
Graph search on array indices.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
