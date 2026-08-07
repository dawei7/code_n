## Description

You are given a 2D integer array `tasks` where $\text{tasks}[i] = [s_{i}, t_{i}]$.

Each $[s_{i}, t_{i}]$ in `tasks` represents a task with start time $s_{i}$ that takes $t_{i}$ units of time to finish.

Return the earliest time at which at least one task is finished.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** tasks = [[1,6],[2,3]]

**Output:** 5

**Explanation:**

The first task starts at time $t = 1$ and finishes at time $1 + 6 = 7$. The second task finishes at time $2 + 3 = 5$. You can finish one task at time 5.

</div>
#### Example 2

<div class="example-block">
**Input:** tasks = [[100,100],[100,100],[100,100]]

**Output:** 200

**Explanation:**

All three tasks finish at time $100 + 100 = 200$.

</div>
### Constraints

- $1 \le \text{tasks.length} \le 100$

- $\text{tasks}[i] = [s_{i}, t_{i}]$

- $1 \le s_{i}, t_{i} \le 100$