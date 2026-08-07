## Description

Table: `prompts`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| prompt      | varchar |
| tokens      | int     |
+-------------+---------+
(user_id, prompt) is the primary key (unique value) for this table.
Each row represents a prompt submitted by a user to an AI system along with the number of tokens consumed.
```

Write a solution to analyze **AI prompt usage patterns** based on the following requirements:

- For each user, calculate the **total number of prompts** they have submitted.

- For each user, calculate the **average tokens used per prompt **(Rounded to `2` decimal places).

- Only include users who have submitted **at least **`3`** prompts**.

- Only include users who have submitted **at least one prompt** with `tokens` **greater than** their own average token usage.

Return *the result table ordered by **average tokens** in **descending** order, and then by $\text{user}_{id}$ in **ascending** order.*

The result format is in the following example.

**Example:**

<div class="example-block">
**Input:**

prompts table:

```
+---------+--------------------------+--------+
| user_id | prompt                   | tokens |
+---------+--------------------------+--------+
| 1       | Write a blog outline     | 120    |
| 1       | Generate SQL query       | 80     |
| 1       | Summarize an article     | 200    |
| 2       | Create resume bullet     | 60     |
| 2       | Improve LinkedIn bio     | 70     |
| 3       | Explain neural networks  | 300    |
| 3       | Generate interview Q&A   | 250    |
| 3       | Write cover letter       | 180    |
| 3       | Optimize Python code     | 220    |
+---------+--------------------------+--------+
```

**Output:**

```
+---------+---------------+------------+
| user_id | prompt_count  | avg_tokens |
+---------+---------------+------------+
| 3       | 4             | 237.5      |
| 1       | 3             | 133.33     |
+---------+---------------+------------+
```

**Explanation:**

- **User 1**:

		<li>Total prompts = 3

- Average tokens = (120 + 80 + 200) / 3 = 133.33

- Has a prompt with 200 tokens, which is greater than the average

- Included in the result

	</li>
- **User 2**:

		<li>Total prompts = 2 (less than the required minimum)

- Excluded from the result

	</li>
- **User 3**:

		<li>Total prompts = 4

- Average tokens = (300 + 250 + 180 + 220) / 4 = 237.5

- Has prompts with 300 and 250 tokens, both greater than the average

- Included in the result

	</li>

The Results table is ordered by avg_tokens in descending order, then by user_id in ascending order

</div>

### Function Contract

**Input table**

- `prompts`: One row per distinct ($\text{user}_{id}$, `prompt`) pair, with the three columns defined in the Description.

All counts and averages are computed within one user's group. The comparison with an individual prompt uses that group's unrounded average; only the displayed $\text{avg}_{tokens}$ value is rounded.

**Result table**

Return exactly these columns:

- $\text{user}_{id}$
- $\text{prompt}_{count}$, the number of that user's rows
- $\text{avg}_{tokens}$, the average of that user's `tokens` values rounded to two decimal places

Include only groups with $\text{prompt}_{count} \ge 3$ and with at least one `tokens` value strictly greater than the group average. Sort by $\text{avg}_{tokens} DESC, \text{user}_{id} ASC$.