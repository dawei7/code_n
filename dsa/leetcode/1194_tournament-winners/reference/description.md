## Description

Table: `Players`

```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| player_id   | int   |
| group_id    | int   |
+-------------+-------+
player_id is the primary key (column with unique values) of this table.
Each row of this table indicates the group of each player.
```

Table: `Matches`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| first_player  | int     |
| second_player | int     |
| first_score   | int     |
| second_score  | int     |
+---------------+---------+
match_id is the primary key (column with unique values) of this table.
Each row is a record of a match, first_player and second_player contain the player_id of each match.
first_score and second_score contain the number of points of the first_player and second_player respectively.
You may assume that, in each match, players belong to the same group.
```

The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the **lowest** $\text{player}_{id}$ wins.

Write a solution to find the winner in each group.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Input tables**

- $Players(\text{player}_{id}, \text{group}_{id})$ supplies every player and that player's group.
- $Matches(\text{match}_{id}, \text{first}_{player}, \text{second}_{player}, \text{first}_{score}, \text{second}_{score})$ supplies both participants and their corresponding points for every match.

Each match contributes $\text{first}_{score}$ to $\text{first}_{player}$ and $\text{second}_{score}$ to $\text{second}_{player}$. Contributions from repeated matches and from both participant positions all belong in the same player total. Match opponents are guaranteed to belong to the same group.

Let $p$ be the number of players, $m$ the number of matches, and $g$ the number of groups.

**Return value**

Return exactly one row per group with columns $\text{group}_{id}$ and $\text{player}_{id}$. Select the maximum-total player independently within each group and break a maximum-total tie by the lowest $\text{player}_{id}$. The result rows may appear in any order.

### Examples

#### Example 1

```
**Input:**
Players table:
+-----------+------------+
| player_id | group_id   |
+-----------+------------+
| 15        | 1          |
| 25        | 1          |
| 30        | 1          |
| 45        | 1          |
| 10        | 2          |
| 35        | 2          |
| 50        | 2          |
| 20        | 3          |
| 40        | 3          |
+-----------+------------+
Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | first_player | second_player | first_score | second_score |
+------------+--------------+---------------+-------------+--------------+
| 1          | 15           | 45            | 3           | 0            |
| 2          | 30           | 25            | 1           | 2            |
| 3          | 30           | 15            | 2           | 0            |
| 4          | 40           | 20            | 5           | 2            |
| 5          | 35           | 50            | 1           | 1            |
+------------+--------------+---------------+-------------+--------------+
**Output:**
+-----------+------------+
| group_id  | player_id  |
+-----------+------------+
| 1         | 15         |
| 2         | 35         |
| 3         | 40         |
+-----------+------------+
```