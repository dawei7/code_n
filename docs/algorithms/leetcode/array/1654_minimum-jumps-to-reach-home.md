# Minimum Jumps to Reach Home

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1654 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Breadth-First Search |
| Official Link | [minimum-jumps-to-reach-home](https://leetcode.com/problems/minimum-jumps-to-reach-home/) |

## Problem Description & Examples
### Goal
Starting at position `0`, jump forward by `a` or backward by `b` while avoiding
forbidden positions and never taking two backward jumps in a row. Find the fewest
jumps needed to reach `x`.

### Function Contract
**Inputs**

- `forbidden`: blocked positions.
- `a`: forward jump length.
- `b`: backward jump length.
- `x`: target position.

**Return value**

The minimum number of jumps, or `-1` if the target cannot be reached.

### Examples
**Example 1**

- Input: `forbidden = [14, 4, 18, 1, 15], a = 3, b = 15, x = 9`
- Output: `3`

**Example 2**

- Input: `forbidden = [8, 3, 16, 6, 12, 20], a = 15, b = 13, x = 11`
- Output: `-1`

**Example 3**

- Input: `forbidden = [1, 6, 2, 14, 5, 17, 4], a = 16, b = 9, x = 7`
- Output: `2`

---

## Underlying Base Algorithm(s)
Run BFS over states `(position, last_jump_was_backward)`. From each state, try a
forward jump and, if the last jump was not backward, a backward jump. Bound the
search above the largest relevant forbidden or target position plus a safety
margin based on `a` and `b`.

---

## Complexity Analysis
- **Time Complexity**: `O(limit)`, where `limit` is the bounded position range.
- **Space Complexity**: `O(limit)`.
