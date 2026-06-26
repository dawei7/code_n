# Cinema Seat Allocation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1386 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Bit Manipulation |
| Official Link | [cinema-seat-allocation](https://leetcode.com/problems/cinema-seat-allocation/) |

## Problem Description & Examples
### Goal
In a cinema with `n` rows and seats `1` through `10`, reserve some seats and then fit as many four-person families as possible. A family can sit in seats `2-5`, `4-7`, or `6-9` within one row.

### Function Contract
**Inputs**

- `n`: the number of cinema rows.
- `reservedSeats`: a list of `[row, seat]` reservations.

**Return value**

The maximum number of four-person families that can be seated.

### Examples
**Example 1**

- Input: `n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`
- Output: `4`

**Example 2**

- Input: `n = 2, reservedSeats = [[2,1],[1,8],[2,6]]`
- Output: `2`

**Example 3**

- Input: `n = 1, reservedSeats = []`
- Output: `2`

---

## Underlying Base Algorithm(s)
Row bitmasking. Rows without relevant reservations contribute `2`; for touched rows, mark seats `2` through `9` and test whether the left, middle, and right family blocks are free.

---

## Complexity Analysis
- **Time Complexity**: `O(r)` where `r` is the number of reserved seats.
- **Space Complexity**: `O(t)` where `t` is the number of rows with relevant reservations.
