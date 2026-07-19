# Consecutive Available Seats

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 603 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/consecutive-available-seats/) |

## Problem Description
### Goal
Given a `Cinema` table whose `seat_id` values identify seats and whose `free` value is `1` for an available seat and `0` for an occupied seat, find all available seats that are part of a consecutive block containing at least two seats.

Return the qualifying `seat_id` values in ascending order. Two seats are consecutive when their identifiers differ by exactly `1`; every seat in a longer available run qualifies, while an available seat with occupied or missing identifiers on both sides does not.

### Function Contract
**Inputs**

- `Cinema(seat_id, free)`: seats in identifier order, where `free = 1` means available and `free = 0` means occupied

**Return value**

- One column, `seat_id`, containing every seat in an available consecutive run of length at least two
- Order identifiers ascending

### Examples
**Example 1**

- Input: seats 3, 4, and 5 are free
- Output: `3, 4, 5`

**Example 2**

- Input: seat 2 is free but seats 1 and 3 are occupied
- Output: no rows

**Example 3**

- Input: seats 1–2 and 5–6 are free
- Output: `1, 2, 5, 6`
