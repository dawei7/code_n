# Game Play Analysis V

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1097 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open](https://leetcode.com/problems/game-play-analysis-v/) |

## Problem Description

### Goal

The `Activity` table records a player's login on a particular date, the device used, and how many games the player completed before logging out. The pair `(player_id, event_date)` is unique, and `games_played` may be zero.

A player's install date is that player's first login date. For each install date $x$, report the number of players whose first login occurred on $x$ and the day-one retention: the fraction of that cohort that logged in again exactly one day after $x$, rounded to two decimal places. Return one row per install date in any order.

### Function Contract

**Input table**

- `Activity(player_id, device_id, event_date, games_played)`: one row per player's activity date; `(player_id, event_date)` is the primary key.

Let $A$ be the number of rows in `Activity`.

**Return value**

A relation with columns `install_dt`, `installs`, and `Day1_retention`. The first is an install date, the second is its cohort size, and the third is its retained-player count divided by that size and rounded to two decimal places.

### Examples

**Example 1**

`Activity`

| player_id | device_id | event_date | games_played |
|---:|---:|---|---:|
| 1 | 2 | 2016-03-01 | 5 |
| 1 | 2 | 2016-03-02 | 6 |
| 2 | 3 | 2017-06-25 | 1 |
| 3 | 1 | 2016-03-01 | 0 |
| 3 | 4 | 2016-07-03 | 5 |

Output:

| install_dt | installs | Day1_retention |
|---|---:|---:|
| 2016-03-01 | 2 | 0.50 |
| 2017-06-25 | 1 | 0.00 |

Players 1 and 3 share the first cohort, but only player 1 returns on `2016-03-02`. Player 3's July activity does not create another install.
