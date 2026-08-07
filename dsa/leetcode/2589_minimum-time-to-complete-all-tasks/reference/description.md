## Description

There is a computer that can run an unlimited number of tasks **at the same time**. You are given a 2D integer array `tasks` where $\text{tasks}[i] = [\text{start}_{i}, \text{end}_{i}, \text{duration}_{i}]$ indicates that the $$i^{\text{th}}$$task should run for a total of$\text{duration}_{i}$seconds (not necessarily continuous) within the **inclusive** time range$[\text{start}_{i}, \text{end}_{i}]$.

You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.

Return *the minimum time during which the computer should be turned on to complete all tasks*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $tasks = [[2,3,1],[4,5,1],[1,5,2]]$
- **Output:** `2`
- **Explanation:**
- The first task can be run in the inclusive time range [2, 2].
- The second task can be run in the inclusive time range [5, 5].
- The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
The computer will be on for a total of 2 seconds.
#### Example 2

- **Input:** $tasks = [[1,3,2],[2,5,3],[5,6,2]]$
- **Output:** `4`
- **Explanation:**
- The first task can be run in the inclusive time range [2, 3].
- The second task can be run in the inclusive time ranges [2, 3] and [5, 5].
- The third task can be run in the two inclusive time range [5, 6].
The computer will be on for a total of 4 seconds.
### Constraints

- $1 \le \text{tasks.length} \le 2000$

- $\text{tasks}[i].length = 3$

- $1 \le \text{start}_{i}, \text{end}_{i} \le 2000$

- $1 \le \text{duration}_{i} \le \text{end}_{i} - \text{start}_{i} + 1$