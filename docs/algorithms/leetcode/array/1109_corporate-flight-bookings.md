# Corporate Flight Bookings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1109 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [corporate-flight-bookings](https://leetcode.com/problems/corporate-flight-bookings/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
Difference array and prefix sum.

---

## Complexity Analysis
- **Time Complexity**: `O(n + b)` where `b` is the number of bookings.
- **Space Complexity**: `O(n)`
