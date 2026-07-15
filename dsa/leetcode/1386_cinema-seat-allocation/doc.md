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

### Required Complexity

- **Time:** $O(r)$
- **Space:** $O(min(n,r))$

<details>
<summary>Approach</summary>

#### General

**Account for untouched rows immediately.** A row with no reservation in seats `2` through `9` can hold both disjoint outer blocks, `2-5` and `6-9`. Because `n` can be enormous, start from two families per row and inspect only rows whose relevant seats are reserved.

**Compress each touched row.** Store a bitmask for reserved seats `2` through `9`. Test that mask against the left, middle, and right block masks. If both outer blocks are free, the row contributes two families. Otherwise it contributes one when any of the three blocks is free, and zero when all are blocked.

The outer blocks are the only pair that can coexist; the middle block overlaps both. Therefore these three tests cover every legal allocation within a row, and summing independent row optima gives the global maximum. Reservations in seats `1` and `10` never affect a family block.

#### Complexity detail

Each of the $r$ reservations is processed once, and each touched row receives constant mask work, so time is $O(r)$. At most $min(n,r)$ rows have relevant reservations, giving $O(\min(n,r))$ space.

#### Alternatives and edge cases

- **Scan every row:** Build reservation masks and examine all `n` rows. It is correct but takes $O(n+r)$ time and is impossible when `n` approaches $10^9$.
- **Store every seat:** A set of coordinate pairs works but uses more state than one bitmask per touched row.
- **Seats 1 and 10:** Ignore them because no allowed family block contains either seat.
- **Only middle block free:** When both outer blocks are blocked, seats `4-7` may still hold one family.
- **Both outer blocks free:** Count two families and do not also count the overlapping middle block.
- **No reservations:** Every row contributes exactly two.
- **All blocks obstructed:** A touched row can contribute zero.

</details>
