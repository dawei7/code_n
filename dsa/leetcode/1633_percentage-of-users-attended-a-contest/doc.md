# Percentage of Users Attended a Contest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1633 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/percentage-of-users-attended-a-contest/) |

## Problem Description
### Goal
The `Users` table contains every platform user, identified by the primary key `user_id`. The `Register` table records contest registrations; its composite primary key `(contest_id, user_id)` guarantees that one user appears at most once for any particular contest.

For every contest that has registrations, compute the percentage of all users who registered for it. Round that percentage to two decimal places. Return `contest_id` and `percentage`, ordered by decreasing percentage; contests tied on percentage must appear by increasing `contest_id`.

### Function Contract
**Inputs**

- `Users(user_id, user_name)`: one row per user, with unique `user_id`.
- `Register(contest_id, user_id)`: one row per contest-user registration, unique by the two columns together.
- Let $u$ be the number of user rows, $r$ the number of registration rows, and $c$ the number of distinct registered contests.

**Return value**

Return columns `contest_id` and `percentage`, with

$$
\textit{percentage}=\operatorname{round}\!\left(100\cdot\frac{\text{registrations for the contest}}{u},2\right).
$$

Sort rows by `percentage` descending and then `contest_id` ascending.

### Examples
**Example 1**

With users 6, 2, and 7, contests 208, 209, and 210 each have all three users; contest 215 has two users and contest 207 has one.

- Output: `[[208,100.0],[209,100.0],[210,100.0],[215,66.67],[207,33.33]]`

**Example 2**

With four total users and contest registration counts 3, 2, and 1:

- Output: `[[10,75.0],[20,50.0],[30,25.0]]`

**Example 3**

With three total users and two registrations for contest 5:

- Output: `[[5,66.67]]`
