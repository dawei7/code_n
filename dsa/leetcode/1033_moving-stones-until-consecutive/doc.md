# Moving Stones Until Consecutive

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1033 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [moving-stones-until-consecutive](https://leetcode.com/problems/moving-stones-until-consecutive/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/moving-stones-until-consecutive/).

### Goal
Three stones sit at distinct integer positions on a number line. In one move, choose an endpoint stone and move it to an unoccupied position strictly between the other two stones. Return the minimum and maximum number of moves needed to make the stones occupy three consecutive positions.

### Function Contract
**Inputs**

- `a`: Position of one stone.
- `b`: Position of one stone.
- `c`: Position of one stone.

**Return value**

Two-element list `[minimum_moves, maximum_moves]`.

### Examples
**Example 1**

- Input: `a = 1, b = 2, c = 5`
- Output: `[1, 2]`

**Example 2**

- Input: `a = 4, b = 3, c = 2`
- Output: `[0, 0]`

**Example 3**

- Input: `a = 3, b = 5, c = 1`
- Output: `[1, 1]`

---

## Solution
### Approach
Sort the three positions as `x < y < z`. If both gaps are `1`, the stones are already consecutive. Otherwise, the minimum is `1` when either gap is at most `2`, because one endpoint can jump into the missing spot and finish immediately; in all other non-consecutive cases the minimum is `2`.

For the maximum, always spend moves shrinking the larger outer gap by one usable position at a time. That gives `max(y - x, z - y) - 1`.

### Complexity Analysis
- **Time Complexity**: `O(1)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
