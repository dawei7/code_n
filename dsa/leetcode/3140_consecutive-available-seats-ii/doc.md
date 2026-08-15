# Consecutive Available Seats II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3140 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/consecutive-available-seats-ii/) |

## Problem Description

### Goal

The `Cinema` table records seats by `seat_id` and indicates whether each seat is available. A value of `1` in `free` means the seat is available, while `0` means it is occupied.

Find every longest sequence of available seats whose IDs are consecutive integers. For each maximum-length sequence, report its first seat ID, last seat ID, and number of seats. If several sequences share the maximum length, include all of them. Order the result by `first_seat_id` in ascending order.

### Function Contract

**Inputs**

- `Cinema`: A table with auto-increment integer column `seat_id` and Boolean column `free`.

Rows may be supplied in any physical order. Consecutiveness is determined by adjacent integer `seat_id` values, not by row insertion order.

**Return value**

Return a table with columns `first_seat_id`, `last_seat_id`, and `consecutive_seats_len`. Include precisely the available runs tied for greatest length, ordered by `first_seat_id` ascending.

### Examples

#### Example 1

Input table `Cinema`:

| seat_id | free |
|---:|---:|
| 1 | 1 |
| 2 | 0 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |

- **Output:** 

| first_seat_id | last_seat_id | consecutive_seats_len |
|---:|---:|---:|
| 3 | 5 | 3 |

Seats 3 through 5 form the unique longest available run.
