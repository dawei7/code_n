# Jump Game V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1340 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [jump-game-v](https://leetcode.com/problems/jump-game-v/) |

## Problem Description & Examples
### Goal
From any starting index, jump left or right up to distance `d`, but only to a strictly lower value and only if every crossed value is also lower than the start. Find the maximum number of indices visitable.

### Function Contract
**Inputs**

- `arr`: integer array.
- `d`: maximum jump distance.

**Return value**

The largest number of positions that can be visited in a valid jump sequence.

### Examples
**Example 1**

- Input: `arr = [6,4,14,6,8,13,9,7,10,6,12]`, `d = 2`
- Output: `4`

**Example 2**

- Input: `arr = [3,3,3,3,3]`, `d = 3`
- Output: `1`

**Example 3**

- Input: `arr = [7,6,5,4,3,2,1]`, `d = 1`
- Output: `7`

---

## Underlying Base Algorithm(s)
Memoized depth-first search on a directed acyclic graph.

---

## Complexity Analysis
- **Time Complexity**: `O(n * d)`
- **Space Complexity**: `O(n)`
