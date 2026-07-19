# Active Users

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1454 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/active-users/) |

## Problem Description
### Goal

`Accounts` identifies each user and stores the user's name. `Logins` records
the calendar dates on which an account logged in; the log may contain duplicate
rows, so multiple login events on one date still represent only one active
day.

An active user is an account that logged in on at least five consecutive
calendar days. Find every active user's `id` and `name`, and return the rows in
ascending order by `id`.

### Function Contract
**Inputs**

- `Accounts(id, name)`: one row per account. `id` is the primary key.
- `Logins(id, login_date)`: login events associating an account with a calendar
  date. Duplicate `(id, login_date)` rows may occur.

Let $A$ be the number of account rows and $L$ the number of distinct
account-date pairs after duplicate login events are removed.

**Return value**

Return a relation with columns `id` and `name`. Include an account exactly when
some run of at least five distinct login dates has no missing calendar day.
Produce at most one row per account and order rows by `id` ascending.

### Examples
**Example 1**

- Input: `Accounts = [(1, "Winston"), (7, "Jonathan")]`, `Logins = [(7, "2020-05-30"), (1, "2020-05-30"), (7, "2020-05-31"), (7, "2020-06-01"), (7, "2020-06-02"), (7, "2020-06-02"), (7, "2020-06-03"), (1, "2020-06-07"), (7, "2020-06-10")]`
- Output: `[(7, "Jonathan")]`
- Explanation: Account `7` has five consecutive distinct dates from May 30
  through June 3. Its duplicate June 2 event counts as the same day.

**Example 2**

- Input: `Accounts = [(2, "Ada")]`, `Logins = [(2, "2022-01-01"), (2, "2022-01-02"), (2, "2022-01-03"), (2, "2022-01-04"), (2, "2022-01-05")]`
- Output: `[(2, "Ada")]`

**Example 3**

- Input: `Accounts = [(3, "Lin")]`, `Logins = [(3, "2022-02-01"), (3, "2022-02-02"), (3, "2022-02-04"), (3, "2022-02-05"), (3, "2022-02-06")]`
- Output: `[]`
- Explanation: Five distinct dates exist, but the gap on February 3 prevents a
  five-day consecutive run.
