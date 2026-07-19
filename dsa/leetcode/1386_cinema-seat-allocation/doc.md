# Cinema Seat Allocation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1386 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/cinema-seat-allocation/) |

## Problem Description

### Goal

A cinema has `n` rows, each containing seats numbered from `1` through `10`. Some seats are already listed in `reserved_seats`. Seat as many four-person families as possible without using a reserved seat or assigning one seat to two families.

Within one row, a family may occupy seats `2-5`, `4-7`, or `6-9`. These are the only permitted four-seat blocks, including the arrangements that place two family members on each side of an aisle. Return the maximum number of families over all rows.

### Function Contract

**Inputs**

- `n`: the number of cinema rows, which may be as large as $10^9$.
- `reserved_seats`: $r$ distinct `[row, seat]` reservations.

**Return value**

- The maximum number of nonoverlapping four-seat family blocks that remain available.

### Examples

**Example 1**

- Input: `n = 3, reserved_seats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`
- Output: `4`

**Example 2**

- Input: `n = 2, reserved_seats = [[2,1],[1,8],[2,6]]`
- Output: `2`

**Example 3**

- Input: `n = 4, reserved_seats = [[4,3],[1,4],[4,6],[1,7]]`
- Output: `4`
