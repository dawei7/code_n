# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1465 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/) |

## Problem Description & Examples
### Goal
Cut a rectangular cake at the given horizontal and vertical positions. Find the maximum possible area of any resulting piece.

### Function Contract
**Inputs**

- `h`: cake height.
- `w`: cake width.
- `horizontalCuts`: horizontal cut positions.
- `verticalCuts`: vertical cut positions.

**Return value**

The largest piece area modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]`
- Output: `4`

**Example 2**

- Input: `h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]`
- Output: `6`

**Example 3**

- Input: `h = 6, w = 7, horizontalCuts = [2], verticalCuts = [2,5]`
- Output: `18`

---

## Underlying Base Algorithm(s)
Sort cuts with the borders included. The largest piece uses the maximum vertical gap times the maximum horizontal gap.

---

## Complexity Analysis
- **Time Complexity**: `O(H log H + V log V)`
- **Space Complexity**: `O(H + V)` if cut lists are copied.
