# Minimum Cost to Move Chips to The Same Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1217 |
| Difficulty | Easy |
| Topics | Array, Math, Greedy |
| Official Link | [minimum-cost-to-move-chips-to-the-same-position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) |

## Problem Description & Examples
### Goal
Move all chips to one position. Moving a chip by two positions costs `0`, while moving it by one position costs `1`. Return the minimum total cost.

### Function Contract
**Inputs**

- `position`: chip positions on a number line.

**Return value**

The minimum cost to gather all chips at one position.

### Examples
**Example 1**

- Input: `position = [1,2,3]`
- Output: `1`

**Example 2**

- Input: `position = [2,2,2,3,3]`
- Output: `2`

**Example 3**

- Input: `position = [1,1000000000]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Parity counting and greedy choice.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
