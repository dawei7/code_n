# Exchange Seats

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 626 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/exchange-seats/) |

## Problem Description
### Goal
Given a `Seat` table whose unique identifiers start at `1` and increase continuously, swap the seat `id` of every two consecutive students: exchange the students at `1` and `2`, at `3` and `4`, and so on.

If the number of students is odd, leave the student with the final `id` in the same seat because no partner remains. Return the resulting `id` and `student` rows ordered by `id` in ascending order; student names move between identifiers, while the identifier sequence itself remains complete.

### Function Contract
**Inputs**

- `Seat(id, student)`: consecutive seat identifiers starting at 1 and their students

**Return value**

- The same ordered `id` values with adjacent student names exchanged
- If the largest ID is odd, its student remains at that seat
- Rows are ordered by `id`

### Examples
**Example 1**

- Input rows: `(1, Abbot)`, `(2, Doris)`, `(3, Emerson)`, `(4, Green)`, `(5, Jeames)`
- Output rows: `(1, Doris)`, `(2, Abbot)`, `(3, Green)`, `(4, Emerson)`, `(5, Jeames)`

**Example 2**

- Input row: `(1, Solo)`
- Output row: `(1, Solo)`
