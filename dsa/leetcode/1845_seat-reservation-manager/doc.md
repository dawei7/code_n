# Seat Reservation Manager

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/seat-reservation-manager/) |
| Frontend ID | 1845 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Design, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Design a reservation manager for $n$ seats numbered consecutively from $1$ through $n$. Every seat begins unreserved, and the object must preserve reservation state across a sequence of method calls.

Whenever a reservation is requested, choose the smallest currently available seat number, mark that seat reserved, and return its number. A separate operation releases a specified reserved seat so that a later reservation may choose it again. Calls are guaranteed to be valid: a reservation always has an available seat, and only a reserved seat is released.

### Function Contract

**Inputs**

- `SeatManager(n)` initializes seats $1$ through $n$ as available, where $1 \le n \le 10^5$.
- `reserve()` takes no argument.
- `unreserve(seatNumber)` receives a currently reserved integer seat in $[1,n]$.
- At most $10^5$ calls are made to `reserve` and `unreserve`.
- Let $q$ be the number of method calls after construction.

**Return value**

- `reserve()` reserves and returns the smallest available seat number.
- `unreserve(seatNumber)` returns nothing and makes that seat available again.
- The constructor returns nothing.
- For an operation trace, represent constructor and `unreserve` results as `null`.

### Examples

**Example 1**

Operations:

`["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]`

Arguments:

`[[5], [], [], [2], [], [], [], [], [5]]`

Output:

`[null, 1, 2, null, 2, 3, 4, 5, null]`

Releasing seat 2 makes it the smallest available seat again, so the next reservation reuses 2 before advancing to 3.

**Example 2**

With one seat, `reserve()`, `unreserve(1)`, and `reserve()` return `1`, nothing, and `1`.

**Example 3**

If seats 1 through 4 are reserved and seats 4 and 2 are then released, the next two reservations return 2 and 4.
