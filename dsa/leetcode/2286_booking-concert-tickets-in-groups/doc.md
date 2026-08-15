# Booking Concert Tickets in Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2286 |
| Difficulty | Hard |
| Topics | Binary Search, Design, Binary Indexed Tree, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/booking-concert-tickets-in-groups/) |

## Problem Description

### Goal

A concert hall has $n$ rows numbered from 0 through $n-1$, with $m$ seats in
each row numbered from 0 through $m-1$. Design a booking system for groups that
restrict every allocated seat to a row no greater than the operation's
`maxRow`. Whenever alternatives exist, allocation must favor the smallest row
number and then the smallest seat numbers in that row.

`gather(k, maxRow)` must place all $k$ spectators in consecutive seats of one
eligible row. It returns the chosen row and the first allocated seat, or an
empty array without changing state if no such block exists.

`scatter(k, maxRow)` may split the group across eligible rows. It succeeds only
if at least $k$ seats are available in the prefix, then fills the earliest rows
and seats first. If capacity is insufficient, it returns `false` without
allocating anything.

### Function Contract

**Inputs**

- `BookMyShow(n, m)`: Creates $n$ rows with $m$ initially empty seats each.
- `gather(k, maxRow)`: Requests $k$ consecutive seats in one row from 0 through `maxRow`.
- `scatter(k, maxRow)`: Requests any $k$ seats across rows 0 through `maxRow`.

Here, $1 \le n \le 5 \cdot 10^4$, $1 \le m,k \le 10^9$, and at most
$q=5 \cdot 10^4$ method calls occur.

**Return value**

Each `gather` returns `[row, firstSeat]` or `[]`. Each `scatter` returns whether
the full group was allocated. Successful calls permanently reserve their
chosen seats.

### Examples

#### Example 1

- Operations: `["BookMyShow", "gather", "gather", "scatter", "scatter"]`
- Arguments: `[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]`
- **Output:** `[null, [0, 0], [], true, false]`

#### Example 2

- Operations: `["BookMyShow", "scatter", "gather"]`
- Arguments: `[[2, 3], [4, 1], [2, 1]]`
- **Output:** `[null, true, [1, 1]]`

#### Example 3

- Operations: `["BookMyShow", "gather", "scatter"]`
- Arguments: `[[1, 1000000000], [999999999, 0], [1, 0]]`
- **Output:** `[null, [0, 0], true]`
