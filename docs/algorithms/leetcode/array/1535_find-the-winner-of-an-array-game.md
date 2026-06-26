# Find the Winner of an Array Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1535 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [find-the-winner-of-an-array-game](https://leetcode.com/problems/find-the-winner-of-an-array-game/) |

## Problem Description & Examples
### Goal
Simulate the array game and return the first value that wins `k` consecutive
rounds. In each round, the first two values compete, the larger stays at the
front, and the smaller moves to the back.

### Function Contract
**Inputs**

- `arr`: an array of distinct integers.
- `k`: the required consecutive win count.

**Return value**

The winning value.

### Examples
**Example 1**

- Input: `arr = [2, 1, 3, 5, 4, 6, 7], k = 2`
- Output: `5`

**Example 2**

- Input: `arr = [3, 2, 1], k = 10`
- Output: `3`

**Example 3**

- Input: `arr = [1, 9, 8, 2, 3, 7, 6, 4, 5], k = 7`
- Output: `9`

---

## Underlying Base Algorithm(s)
Keep the current champion and its consecutive win count while scanning challengers
from left to right. A larger challenger becomes the new champion with one win;
otherwise the champion gains another win. The maximum array value will
eventually win, so stop when the count reaches `k` or the scan ends.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
