# Corporate Flight Bookings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1109 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [corporate-flight-bookings](https://leetcode.com/problems/corporate-flight-bookings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/corporate-flight-bookings/).

### Goal
Each booking adds seats to every flight in an inclusive flight-number range. Return the final booked-seat count for flights `1` through `n`.

### Function Contract
**Inputs**

- `bookings`: list of `[first, last, seats]` updates.
- `n`: number of flights.

**Return value**

Array where index `i` stores the total seats booked on flight `i + 1`.

### Examples
**Example 1**

- Input: `bookings = [[1,2,10],[2,3,20],[2,5,25]]`, `n = 5`
- Output: `[10,55,45,25,25]`

**Example 2**

- Input: `bookings = [[1,1,5],[2,2,7]]`, `n = 2`
- Output: `[5,7]`

**Example 3**

- Input: `bookings = [[1,3,4],[3,3,6]]`, `n = 3`
- Output: `[4,4,10]`

---

## Solution
### Approach
Difference array and prefix sum.

### Complexity Analysis
- **Time Complexity**: `O(n + b)` where `b` is the number of bookings.
- **Space Complexity**: `O(n)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1109: Corporate Flight Bookings."""


def solve(bookings: list[list[int]], n: int) -> list[int]:
    diff = [0] * (n + 1)
    for first, last, seats in bookings:
        diff[first - 1] += seats
        diff[last] -= seats

    answer = []
    current = 0
    for i in range(n):
        current += diff[i]
        answer.append(current)
    return answer
```
</details>
