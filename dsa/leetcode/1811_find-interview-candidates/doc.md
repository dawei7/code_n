# Find Interview Candidates

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-interview-candidates/) |
| Frontend ID | 1811 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Contests` table records each contest's unique `contest_id` and the user IDs of its gold, silver, and bronze medalists. Contest IDs advance consecutively without skipped values. The `Users` table maps each unique `user_id` to a `name` and `mail`.

A user is an interview candidate when either of two independent rules holds: the user won any medal in at least three consecutive contests, or the user won gold in at least three different contests even when those contests are not consecutive. Report the `name` and `mail` of every qualifying user. A user satisfying both rules must still appear only once, and result order is unrestricted.

### Function Contract

**Inputs**

- `Contests(contest_id, gold_medal, silver_medal, bronze_medal)`: one row per contest with a unique ID and three medalist user IDs. Consecutive contests have consecutive IDs with no skipped ID.
- `Users(user_id, mail, name)`: one row per user, keyed by `user_id`.
- Let $C$ be the number of contests and $U$ the number of users.

**Return value**

- Return columns `name` and `mail`.
- Include each user once if they won any medal in a run of at least three consecutive contests or won gold in at least three distinct contests.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: contests `190` through `196` with medalists `[[1,5,2],[2,3,5],[5,2,3],[1,3,5],[4,5,2],[4,2,1],[1,5,2]]`
- Output: users Sarah, Bob, Alice, and Quarz with their mail addresses

Sarah has three gold medals. Bob, Alice, and Quarz each have a run of at least three consecutive contests with some medal.

**Example 2**

- Input: user `7` wins gold in contests `10`, `20`, and `30`
- Output: user `7`'s `name` and `mail`

The gold-medal rule does not require consecutive contests.

**Example 3**

- Input: user `8` wins medals in contests `1`, `2`, and `4`
- Output: no row for user `8`

Three medals alone are insufficient when they are neither all gold nor spread across three consecutive contest IDs.
