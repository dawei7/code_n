# Human Traffic of Stadium

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 601 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/human-traffic-of-stadium/) |

## Problem Description
### Goal
Given a `Stadium` table containing a visit identifier, visit date, and number of people, find every record that belongs to a sequence of three or more rows with consecutive `id` values. Every row in the qualifying sequence must have `people` greater than or equal to `100`.

Return the original `id`, `visit_date`, and `people` columns for all rows in every qualifying sequence, ordered by `visit_date` in ascending order. A long sequence contributes all of its rows, including endpoints, while an isolated busy day or a run of only two busy identifiers does not qualify.

### Function Contract
**Inputs**

- `Stadium(id, visit_date, people)`: daily stadium attendance records ordered by increasing identifier

**Return value**

- Columns `id`, `visit_date`, and `people` for all rows in qualifying consecutive-ID runs
- Order results by `visit_date` ascending

### Examples
**Example 1**

- Input: identifiers 5 through 8 each have at least 100 visitors
- Output: all four rows 5, 6, 7, and 8

**Example 2**

- Input: only identifiers 2 and 3 meet the threshold consecutively
- Output: no rows

**Example 3**

- Input: identifiers 1 through 3 qualify, identifier 4 is below 100, and 5 through 7 qualify
- Output: rows 1 through 3 and 5 through 7
