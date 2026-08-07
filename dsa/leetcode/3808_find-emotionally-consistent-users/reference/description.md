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

- For each user, count the total number of reactions they have given.

- Only include users who have reacted to **at least **`5`** different content items**.

- A user is considered **emotionally consistent** if **at least **`60%` of their reactions are of the **same type**.

Return *the result table ordered by* $\text{reaction}_{ratio}$ *in **descending** order and then by* $\text{user}_{id}$ *in **ascending** order*.

**Note:**

- $\text{reaction}_{ratio}$ should be rounded to `2` decimal places

The result format is in the following example.

**Example:**

<div class="example-block">
**Input:**

reactions table:

```
+---------+------------+----------+
| user_id | content_id | reaction |
+---------+------------+----------+
| 1       | 101        | like     |
| 1       | 102        | like     |
| 1       | 103        | like     |
| 1       | 104        | wow      |
| 1       | 105        | like     |
| 2       | 201        | like     |
| 2       | 202        | wow      |
| 2       | 203        | sad      |
| 2       | 204        | like     |
| 2       | 205        | wow      |
| 3       | 301        | love     |
| 3       | 302        | love     |
| 3       | 303        | love     |
| 3       | 304        | love     |
| 3       | 305        | love     |
+---------+------------+----------+
```

**Output:**

```
+---------+-------------------+----------------+
| user_id | dominant_reaction | reaction_ratio |
+---------+-------------------+----------------+
| 3       | love              | 1.00           |
| 1       | like              | 0.80           |
+---------+-------------------+----------------+
```

**Explanation:**

- **User 1**:

		<li>Total reactions = 5

- like appears 4 times

- reaction_ratio = 4 / 5 = 0.80

- Meets the 60% consistency requirement

	</li>
- **User 2**:

		<li>Total reactions = 5

- Most frequent reaction appears only 2 times

- reaction_ratio = 2 / 5 = 0.40

- Does not meet the consistency requirement

	</li>
- **User 3**:

		<li>Total reactions = 5

- 'love' appears 5 times

- reaction_ratio = 5 / 5 = 1.00

- Meets the consistency requirement

	</li>

The Results table is ordered by reaction_ratio in descending order, then by user_id in ascending order.

</div>

### Function Contract

**Input table**

- `reactions`: One row per distinct ($\text{user}_{id}$, $\text{content}_{id}$) pair, with the three columns defined in the Description.

For a user with $R_u$ reaction rows, let $C_{u,t}$ be the number whose `reaction` is type $t$. The user qualifies only when $R_u \ge 5$ and some type satisfies

$\frac{C_{u,t}}{R_u} \ge 0.60.$

Because 60% is greater than half, at most one reaction type can satisfy this condition for a user.

**Result table**

Return exactly these columns:

- $\text{user}_{id}$
- $\text{dominant}_{reaction}$, the qualifying reaction type
- $\text{reaction}_{ratio}$, the qualifying type's count divided by the user's total reaction count

Include one row for each qualifying user. Sort the rows by $\text{reaction}_{ratio} DESC, \text{user}_{id} ASC$.