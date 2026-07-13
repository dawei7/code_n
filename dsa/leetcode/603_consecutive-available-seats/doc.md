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

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Expose each row's immediate neighbors**

Order by `seat_id` and use `LAG` and `LEAD` to attach the preceding and following identifiers and availability flags to every seat.

**Require a truly consecutive free neighbor**

Keep the current row only when it is free and either the previous row is free with identifier `seat_id - 1`, or the next row is free with identifier `seat_id + 1`. Checking identifiers makes the logic robust even if a data set has a gap.

**Why every qualifying seat is returned**

A seat belongs to a consecutive available pair exactly when one of its numeric neighbors exists and is free. The two window comparisons test those two possibilities directly. Runs longer than two satisfy the condition at their endpoints through one neighbor and at interior seats through both, so every run member appears exactly once.

#### Complexity detail

For `n` seats, the window ordering generally costs $O(n \log n)$ time and $O(n)$ working space. Filtering and final output ordering fit within that bound.

#### Alternatives and edge cases

- **Self-join adjacent identifiers:** join free seats on an absolute identifier difference of one and union both endpoints; it is correct but requires deduplication.
- **Windowed three-row sum:** works when seat identifiers are guaranteed gapless, but explicit identifier checks are more robust.
- **Correlated neighbor existence:** is direct but may rescan the table for every seat and take $O(n^2)$ time without an index.
- **Isolated free seat:** is excluded.
- **Exactly two free seats:** both are returned.
- **Long free run:** every seat in the run is returned.
- **Occupied seat between free seats:** breaks adjacency.
- **Identifier gap:** does not create a consecutive pair.
- **Output order:** must be ascending by seat identifier.

</details>
