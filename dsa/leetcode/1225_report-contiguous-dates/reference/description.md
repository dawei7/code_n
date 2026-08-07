### 1. Description

Table: `Failed`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| fail_date    | date    |
+--------------+---------+
fail_date is the primary key (column with unique values) for this table.
This table contains the days of failed tasks.
```

Table: `Succeeded`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| success_date | date    |
+--------------+---------+
success_date is the primary key (column with unique values) for this table.
This table contains the days of succeeded tasks.
```

A system is running one task **every day**. Every task is independent of the previous tasks. The tasks can fail or succeed.

Write a solution to report the $\text{period}_{state}$ for each continuous interval of days in the period from `2019-01-01` to `2019-12-31`.

$\text{period}_{state}$ is *'*`failed'`* *if tasks in this interval failed or `'succeeded'` if tasks in this interval succeeded. Interval of days are retrieved as $\text{start}_{date}$ and $\text{end}_{date}.$

Return the result table ordered by $\text{start}_{date}$.

The result format is in the following example.

### 2. Function Contract

**Input tables**

$Failed(\text{fail}_{date})$ and $Succeeded(\text{success}_{date})$ contain unique dates for the corresponding task outcomes. Let $d$ be the combined number of rows whose dates fall from `2019-01-01` through `2019-12-31`, inclusive.

**Return value**

- Return exactly the columns $\text{period}_{state}$, $\text{start}_{date}$, and $\text{end}_{date}$.
- Produce one row for every maximal continuous interval of recorded days having the same state.
- Use only the lowercase labels `failed` and `succeeded`.
- For a one-day interval, return the same date as both endpoints.
- Ignore dates outside 2019 when forming the reported intervals.
- Order the rows by $\text{start}_{date}$ in ascending order.

### 3. Examples

#### Example 1

```
**Input:**
Failed table:
+-------------------+
| fail_date         |
+-------------------+
| 2018-12-28        |
| 2018-12-29        |
| 2019-01-04        |
| 2019-01-05        |
+-------------------+
Succeeded table:
+-------------------+
| success_date      |
+-------------------+
| 2018-12-30        |
| 2018-12-31        |
| 2019-01-01        |
| 2019-01-02        |
| 2019-01-03        |
| 2019-01-06        |
+-------------------+
**Output:**
+--------------+--------------+--------------+
| period_state | start_date   | end_date     |
+--------------+--------------+--------------+
| succeeded    | 2019-01-01   | 2019-01-03   |
| failed       | 2019-01-04   | 2019-01-05   |
| succeeded    | 2019-01-06   | 2019-01-06   |
+--------------+--------------+--------------+
**Explanation:**
The report ignored the system state in 2018 as we care about the system in the period 2019-01-01 to 2019-12-31.
From 2019-01-01 to 2019-01-03 all tasks succeeded and the system state was "succeeded".
From 2019-01-04 to 2019-01-05 all tasks failed and the system state was "failed".
From 2019-01-06 to 2019-01-06 all tasks succeeded and the system state was "succeeded".
```