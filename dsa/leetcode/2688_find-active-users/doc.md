# Find Active Users

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2688 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/find-active-users/) |

## Problem Description

### Goal

The `Users` table records purchases. A row identifies the user, purchased item, purchase timestamp, and amount. The table can contain duplicate rows; each row still represents a purchase occurrence.

A user is active when one of their purchases is followed by another purchase no more than seven days later. The seven-day boundary is inclusive, so purchases exactly seven days apart qualify, as do two purchases on the same date. Return the identifiers of all active users in any order, with each qualifying user appearing once.

### Function Contract

**Input table**

- `Users(user_id, item, created_at, amount)`: Each row describes one purchase. Duplicate records are allowed.

**Return value**

Return one `user_id` row for every user who has two purchase rows whose timestamps are at most seven calendar days apart. Result order is unrestricted.

### Examples

#### Example 1

- **Input:** User `6` bought items on `2021-09-10` and `2021-09-14`; user `4` bought on `2021-09-02` and `2021-09-13`; users `5` and `8` bought once.
- **Output:** `[[6]]`
- **Explanation:** Only user `6` has a second purchase within seven days of another purchase.

#### Example 2

- **Input:** One user purchases on `2024-01-01` and `2024-01-08`.
- **Output:** That user's identifier, because the gap is exactly seven days.

#### Example 3

- **Input:** Two purchase rows for one user share the same `created_at` value.
- **Output:** That user's identifier, because the zero-day gap qualifies.
