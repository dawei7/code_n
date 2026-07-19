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

### Required Complexity

- **Time:** $O(q\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Represent untouched seats as a frontier**

Initially the available seats are the contiguous range $[1,n]$. There is no need to store that entire range. Keep `next_seat`, the smallest seat never reserved before. When no explicitly released seat is waiting, `next_seat` is necessarily the smallest available number: all smaller numbers have already been handed out and not subsequently released.

**Keep released seats in a min-heap**

When `unreserve(seatNumber)` is called, push that number into a min-heap. The validity guarantee prevents duplicate available copies because the same seat cannot be released twice without an intervening reservation.

On `reserve()`, prefer the heap when it is nonempty. Every released seat is below `next_seat`, since it must have been reserved earlier, so the heap minimum is smaller than every never-used seat. Pop and return that minimum. If the heap is empty, return `next_seat` and advance the frontier.

The representation partitions available seats into released numbers in the heap and the untouched suffix beginning at `next_seat`. Reserved seats belong to neither set. This partition is maintained by both operations, and selecting the smaller source as described always yields the globally smallest available seat.

#### Complexity detail

Construction takes $O(1)$ time. Reserving a never-used seat takes $O(1)$; reserving a released seat and every `unreserve` take $O(\log n)$ heap time. Across $q$ calls, the upper bound is $O(q\log n)$. At most $n$ released seats can be stored, so space is $O(n)$.

#### Alternatives and edge cases

- **Heap all seats initially:** Heapifying $1$ through $n$ gives the same operation bounds but spends $O(n)$ initialization space and time even if few seats are touched.
- **Boolean array with linear scan:** State updates are simple, but repeatedly locating the first available seat can take $O(n)$ per reservation.
- **Balanced ordered set:** It supports minimum removal and insertion in $O(\log n)$ but still requires either materializing untouched seats or pairing it with a frontier.
- **Released seat before frontier:** Any released number must be preferred to the never-used suffix.
- **Out-of-order releases:** Heap order, rather than release order, determines reuse.
- **Single seat:** Releasing its only seat permits it to be reserved again.
- **Full occupancy:** The contract guarantees `reserve()` is not called when no seat is available.
- **Valid release:** No duplicate-availability guard is needed because `unreserve` is called only for a reserved seat.

</details>
