# Stone Game V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1563 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [stone-game-v](https://leetcode.com/problems/stone-game-v/) |

## Problem Description & Examples
### Goal
Split the row of stones repeatedly to maximize Alice's score. At each split, Bob
removes the side with the larger sum; if both sums are equal, Alice may choose
which side remains. Alice gains the sum of the side that remains after each
split.

### Function Contract
**Inputs**

- `stoneValue`: the values of the stones in order.

**Return value**

The maximum score Alice can guarantee.

### Examples
**Example 1**

- Input: `stoneValue = [6, 2, 3, 4, 5, 5]`
- Output: `18`

**Example 2**

- Input: `stoneValue = [7, 7, 7, 7, 7, 7, 7]`
- Output: `28`

**Example 3**

- Input: `stoneValue = [4]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Use prefix sums and interval dynamic programming. For every interval, try each
split point, compare the left and right sums, and recurse only into the side that
could remain. If the sums are equal, take the better of the two recursive
choices.

---

## Complexity Analysis
- **Time Complexity**: `O(n^3)` for the direct interval DP.
- **Space Complexity**: `O(n^2)`.
