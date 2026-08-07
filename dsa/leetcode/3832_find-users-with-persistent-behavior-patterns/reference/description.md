## Description

Table: `activity`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| action_date  | date    |
| action       | varchar |
+--------------+---------+
(user_id, action_date, action) is the primary key (unique value) for this table.
Each row represents a user performing a specific action on a given date.
```

Write a solution to identify **behaviorally stable users** based on the following definition:

- A user is considered **behaviorally stable** if there exists a sequence of **at least **`5`** consecutive days** such that:

		<li>The user performed **exactly one action per day** during that period.

- The **action is the same** on all those consecutive days.

	</li>
- If a user has multiple qualifying sequences, only consider the sequence with the **maximum length**.

Return *the result table ordered by* $\text{streak}_{length}$ *in **descending** order*,* then by *$\text{user}_{id}$ *in **ascending** order*.

The result format is in the following example.

**Example:**

<div class="example-block">
**Input:**

activity table:

```
+---------+-------------+--------+
| user_id | action_date | action |
+---------+-------------+--------+
| 1       | 2024-01-01  | login  |
| 1       | 2024-01-02  | login  |
| 1       | 2024-01-03  | login  |
| 1       | 2024-01-04  | login  |
| 1       | 2024-01-05  | login  |
| 1       | 2024-01-06  | logout |
| 2       | 2024-01-01  | click  |
| 2       | 2024-01-02  | click  |
| 2       | 2024-01-03  | click  |
| 2       | 2024-01-04  | click  |
| 3       | 2024-01-01  | view   |
| 3       | 2024-01-02  | view   |
| 3       | 2024-01-03  | view   |
| 3       | 2024-01-04  | view   |
| 3       | 2024-01-05  | view   |
| 3       | 2024-01-06  | view   |
| 3       | 2024-01-07  | view   |
+---------+-------------+--------+
```

**Output:**

```
+---------+--------+---------------+------------+------------+
| user_id | action | streak_length | start_date | end_date   |
+---------+--------+---------------+------------+------------+
| 3       | view   | 7             | 2024-01-01 | 2024-01-07 |
| 1       | login  | 5             | 2024-01-01 | 2024-01-05 |
+---------+--------+---------------+------------+------------+
```

**Explanation:**

- **User 1**:

		<li>Performed `login` from 2024-01-01 to 2024-01-05 on consecutive days

- Each day has exactly one action, and the action is the same

- Streak length = 5 (meets minimum requirement)

- The action changes on 2024-01-06, ending the streak

	</li>
- **User 2**:

		<li>Performed `click` for only 4 consecutive days

- Does not meet the minimum streak length of 5

- Excluded from the result

	</li>
- **User 3**:

		<li>Performed `view` for 7 consecutive days

- This is the longest valid sequence for this user

- Included in the result

	</li>

The Results table is ordered by streak_length in descending order, then by user_id in ascending order

</div>

### Function Contract

**Inputs**

- `activity`: The activity table described above.

Let $R$ denote the number of rows in `activity`. A calendar date is eligible for a user's streak only when exactly one table row exists for that ($\text{user}_{id}$, $\text{action}_{date}$) pair. A date with two or more distinct actions is ineligible and separates runs on either side of it.

Consecutive means adjacent calendar dates, not merely adjacent records after sorting. A change in `action`, a missing date, or an ineligible multi-action date ends the current run.

**Return value**

Return an ordered table with columns:

- $\text{user}_{id}$
- `action`
- $\text{streak}_{length}$
- $\text{start}_{date}$
- $\text{end}_{date}$

Only users whose selected maximum run has length at least five appear. The primary order is $\text{streak}_{length}$ descending and the secondary order is $\text{user}_{id}$ ascending.