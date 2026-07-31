# Arrange Table by Gender

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2308 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/arrange-table-by-gender/) |

## Problem Description

### Goal

The `Genders` table contains one row per user. Its `gender` value is one of `female`, `male`, or `other`, and the table contains the same number of users in all three groups.

Rearrange every row into repeating groups ordered as `female`, then `other`, then `male`. Within each gender, users must appear by ascending `user_id`. Return both original columns in exactly this interleaved order; the sequence of output rows is part of the required result.

### Function Contract

**Inputs**

- `Genders`: A table with unique integer `user_id` values and a `gender` column whose value is `female`, `male`, or `other`.

The three gender categories contain equal numbers of rows.

**Return value**

Return the `user_id` and `gender` of every input row. Alternate categories in the order `female`, `other`, `male`, while sorting the IDs within each category in ascending order.

### Examples

**Example 1**

- Input: `Genders = [(4,"male"),(7,"female"),(2,"other"),(5,"male"),(3,"female"),(8,"male"),(6,"other"),(1,"other"),(9,"female")]`
- Output: `[(3,"female"),(1,"other"),(4,"male"),(7,"female"),(2,"other"),(5,"male"),(9,"female"),(6,"other"),(8,"male")]`

The IDs within each category are ascending, and the three categories repeat in the required order.
