## Description

Table: `reactions`

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| content_id   | int     |
| reaction     | varchar |
+--------------+---------+
(user_id, content_id) is the primary key (unique value) for this table.
Each row represents a reaction given by a user to a piece of content.

```

Write a solution to identify **emotionally consistent users** based on the following requirements:

<ul>
	<li>For each user, count the total number of reactions they have given.</li>
	<li>Only include users who have reacted to **at least **`5`** different content items**.</li>
	<li>A user is considered **emotionally consistent** if **at least **`60%` of their reactions are of the **same type**.</li>
</ul>

Return *the result table ordered by* `reaction_ratio` *in **descending** order and then by* `user_id` *in **ascending** order*.

**Note:**

<ul>
	<li>`reaction_ratio` should be rounded to `2` decimal places</li>
</ul>

The result format is in the following example.
