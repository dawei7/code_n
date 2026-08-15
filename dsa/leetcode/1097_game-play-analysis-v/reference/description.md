### 1. Description

Table: `Activity`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
```

The **install date** of a player is the first login day of that player.

We define **day one retention** of some date `x` to be the number of players whose **install date** is `x` and they logged back in on the day right after `x`, divided by the number of players whose install date is `x`, rounded to `2` decimal places.

Write a solution to report for each install date, the number of players that installed the game on that day, and the **day one retention**.

Return the result table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Input table**

- $Activity(\text{player}_{id}, \text{device}_{id}, \text{event}_{date}, \text{games}_{played})$: one row for a player's login on a particular date, with ($\text{player}_{id}$, $\text{event}_{date}$) as the composite primary key.

For each player, let $\text{install}_{dt}$ be the minimum $\text{event}_{date}$ in that player's activity. The player contributes once to the cohort for that date. A cohort member is retained only if another row for the same $\text{player}_{id}$ has an $\text{event}_{date}$ exactly one calendar day after $\text{install}_{dt}$; a return two or more days later does not count. The device and the number of games played do not affect either membership or retention.

**Return value**

- $\text{install}_{dt}$: the cohort's common first-login date.
- `installs`: the number of players in that cohort.
- $\text{Day1}_{retention}$: the number of those players with an exact next-day login divided by `installs`, rounded to two decimal places.

Produce one result row per install date. Result order is unrestricted. If `Activity` is empty, the result is empty.

### 3. Examples

#### Example 1

```
- **Input:** 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-01 | 0            |
| 3         | 4         | 2016-07-03 | 5            |
+-----------+-----------+------------+--------------+
- **Output:** 
+------------+----------+----------------+
| install_dt | installs | Day1_retention |
+------------+----------+----------------+
| 2016-03-01 | 2        | 0.50           |
| 2017-06-25 | 1        | 0.00           |
+------------+----------+----------------+
- **Explanation:** Player 1 and 3 installed the game on 2016-03-01 but only player 1 logged back in on 2016-03-02 so the day 1 retention of 2016-03-01 is 1 / 2 = 0.50
Player 2 installed the game on 2017-06-25 but didn't log back in on 2017-06-26 so the day 1 retention of 2017-06-25 is 0 / 1 = 0.00
```
