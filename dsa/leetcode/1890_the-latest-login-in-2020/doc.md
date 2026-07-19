# The Latest Login in 2020

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/the-latest-login-in-2020/) |
| Frontend ID | 1890 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Logins` table records the date and time of every user login. Its composite primary key guarantees that the same user cannot have two rows with the identical timestamp, although a user may have any number of logins across different years.

Report each user who logged in at least once during calendar year 2020. For every included user, return only their latest 2020 timestamp under the column name `last_stamp`. Logins before or after 2020 must not influence the selected timestamp, and users with no 2020 login must be omitted. Result rows may appear in any order.

### Function Contract

**Inputs**

- `Logins(user_id, time_stamp)`: one row per distinct user-and-timestamp pair.
- `user_id` is an integer and `time_stamp` is a datetime value.
- Let $R$ be the number of login rows and $U$ the number of users with at least one 2020 login.

**Return value**

- Return columns `user_id` and `last_stamp`.
- Include exactly one row for each qualifying user, with their maximum timestamp in 2020.
- Output order is not significant.

### Examples

**Example 1**

- Input: user `6` logs in during 2019, 2020, and 2021; user `8` logs in twice during 2020; user `14` logs in only outside 2020.
- Output: user `6` with `2020-06-30 15:06:07` and user `8` with `2020-12-30 00:46:50`; user `14` is omitted.

**Example 2**

- Input: `(1, "2020-01-01 00:00:00")`
- Output: `(1, "2020-01-01 00:00:00")`

The first instant of 2020 is included.

**Example 3**

- Input: `(2, "2021-01-01 00:00:00")`
- Output: no rows.

The first instant of 2021 is outside the requested year.
