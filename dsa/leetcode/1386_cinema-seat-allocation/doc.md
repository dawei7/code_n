# Cinema Seat Allocation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1386 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [cinema-seat-allocation](https://leetcode.com/problems/cinema-seat-allocation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/cinema-seat-allocation/).

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

## Solution
### Approach
Row bitmasking. Rows without relevant reservations contribute `2`; for touched rows, mark seats `2` through `9` and test whether the left, middle, and right family blocks are free.

### Complexity Analysis
- **Time Complexity**: `O(r)` where `r` is the number of reserved seats.
- **Space Complexity**: `O(t)` where `t` is the number of rows with relevant reservations.

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1386: Cinema Seat Allocation."""

from collections import defaultdict


def solve(n: int, reserved_seats: list[list[int]]) -> int:
    occupied: dict[int, int] = defaultdict(int)
    for row, seat in reserved_seats:
        if 2 <= seat <= 9:
            occupied[row] |= 1 << seat

    answer = (n - len(occupied)) * 2
    left = sum(1 << seat for seat in range(2, 6))
    middle = sum(1 << seat for seat in range(4, 8))
    right = sum(1 << seat for seat in range(6, 10))

    for mask in occupied.values():
        can_left = mask & left == 0
        can_right = mask & right == 0
        if can_left and can_right:
            answer += 2
        elif can_left or can_right or mask & middle == 0:
            answer += 1
    return answer
```
</details>
