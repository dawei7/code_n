# Add Minimum Number of Rungs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1936 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [add-minimum-number-of-rungs](https://leetcode.com/problems/add-minimum-number-of-rungs/) |

## Problem Description & Examples
### Goal
You are climbing a ladder whose existing rung heights are listed in increasing order. Add the fewest extra rungs so every jump between consecutive reachable heights, starting from ground `0`, is at most `dist`.

### Function Contract
**Inputs**

- `rungs`: sorted positive rung heights.
- `dist`: the maximum allowed climb distance in one move.

**Return value**

Return the minimum number of new rungs that must be inserted.

### Examples
**Example 1**

- Input: `rungs = [1,3,5,10], dist = 2`
- Output: `2`

**Example 2**

- Input: `rungs = [3,6,8,10], dist = 3`
- Output: `0`

**Example 3**

- Input: `rungs = [3,4,6,7], dist = 2`
- Output: `1`

---

## Underlying Base Algorithm(s)
Scan gaps from the previous height to the next rung. For a gap `g`, the number of inserted rungs needed is `(g - 1) // dist`, because the existing endpoint can be reached after those intermediate steps.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
