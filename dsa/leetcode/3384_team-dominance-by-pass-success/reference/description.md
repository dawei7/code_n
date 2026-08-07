## Description

Table: `Teams`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| player_id   | int     |
| team_name   | varchar |
+-------------+---------+
player_id is the unique key for this table.
Each row contains the unique identifier for player and the name of one of the teams participating in that match.
```

Table: `Passes`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| pass_from   | int     |
| time_stamp  | varchar |
| pass_to     | int     |
+-------------+---------+
(pass_from, time_stamp) is the primary key for this table.
pass_from is a foreign key to player_id from Teams table.
Each row represents a pass made during a match, time_stamp represents the time in minutes (00:00-90:00) when the pass was made,
pass_to is the player_id of the player receiving the pass.
```

Write a solution to calculate the **dominance score** for each team in** both halves of the match**. The rules are as follows:

- A match is divided into two halves: **first half** (`00:00`-`45:00` minutes) and **second half **(`45:01`-`90:00` minutes)

- The dominance score is calculated based on successful and intercepted passes:

		<li>When pass_to is a player from the **same team**: +`1` point

- When pass_to is a player from the **opposing team** (interception): `-1` point

	</li>
- A higher dominance score indicates better passing performance

Return *the result table ordered **by* $\text{team}_{name}$ and $\text{half}_{number}$ *in **ascending** order*.

The result format is in the following example.

**Example:**

<div class="example-block">
**Input:**

Teams table:

```
+------------+-----------+
| player_id  | team_name |
+------------+-----------+
| 1          | Arsenal   |
| 2          | Arsenal   |
| 3          | Arsenal   |
| 4          | Chelsea   |
| 5          | Chelsea   |
| 6          | Chelsea   |
+------------+-----------+
```

Passes table:

```
+-----------+------------+---------+
| pass_from | time_stamp | pass_to |
+-----------+------------+---------+
| 1         | 00:15      | 2       |
| 2         | 00:45      | 3       |
| 3         | 01:15      | 1       |
| 4         | 00:30      | 1       |
| 2         | 46:00      | 3       |
| 3         | 46:15      | 4       |
| 1         | 46:45      | 2       |
| 5         | 46:30      | 6       |
+-----------+------------+---------+
```

**Output:**

```
+-----------+-------------+-----------+
| team_name | half_number | dominance |
+-----------+-------------+-----------+
| Arsenal   | 1           | 3         |
| Arsenal   | 2           | 1         |
| Chelsea   | 1           | -1        |
| Chelsea   | 2           | 1         |
+-----------+-------------+-----------+
```

**Explanation:**

- **First Half (00:00-45:00):**

		<li>Arsenal's passes:

			<li>1 → 2 (00:15): Successful pass (+1)

- 2 → 3 (00:45): Successful pass (+1)

- 3 → 1 (01:15): Successful pass (+1)

		</li>
- Chelsea's passes:

			<li>4 → 1 (00:30): Intercepted by Arsenal (-1)

		</li>

	</li>
- **Second Half (45:01-90:00):**

		<li>Arsenal's passes:

			<li>2 → 3 (46:00): Successful pass (+1)

- 3 → 4 (46:15): Intercepted by Chelsea (-1)

- 1 → 2 (46:45): Successful pass (+1)

		</li>
- Chelsea's passes:

			<li>5 → 6 (46:30): Successful pass (+1)

		</li>

	</li>
- The results are ordered by team_name and then half_number

</div>

### Function Contract

- Refer to method signature.