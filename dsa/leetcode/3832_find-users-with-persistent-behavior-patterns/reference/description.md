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

<ul>
	<li>A user is considered **behaviorally stable** if there exists a sequence of **at least **`5`** consecutive days** such that:

	<ul>
		<li>The user performed **exactly one action per day** during that period.</li>
		<li>The **action is the same** on all those consecutive days.</li>
	</ul>
	</li>
	<li>If a user has multiple qualifying sequences, only consider the sequence with the **maximum length**.</li>
</ul>

Return *the result table ordered by* `streak_length` *in **descending** order*,* then by *`user_id` *in **ascending** order*.

The result format is in the following example.
