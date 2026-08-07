### 1. Description

There are `n` employees, each with a unique id from `0` to $n - 1$.

You are given a 2D integer array `logs` where $\text{logs}[i] = [\text{id}_{i}, \text{leaveTime}_{i}]$ where:

- $\text{id}_{i}$ is the id of the employee that worked on the $$i^{\text{th}}$$ task, and

- $\text{leaveTime}_{i}$ is the time at which the employee finished the $$i^{\text{th}}$$ task. All the values $\text{leaveTime}_{i}$ are **unique**.

Note that the $$i^{\text{th}}$$ task starts the moment right after the $(i - 1)^th$ task ends, and the $0^th$ task starts at time `0`.

Return *the id of the employee that worked the task with the longest time.* If there is a tie between two or more employees, return* the **smallest** id among them*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]$
- **Output:** `1`
- **Explanation:**
Task 0 started at 0 and ended at 3 with 3 units of times.
Task 1 started at 3 and ended at 5 with 2 units of times.
Task 2 started at 5 and ended at 9 with 4 units of times.
Task 3 started at 9 and ended at 15 with 6 units of times.
The task with the longest time is task 3 and the employee with id 1 is the one that worked on it, so we return 1.
#### Example 2

- **Input:** $n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]$
- **Output:** `3`
- **Explanation:**
Task 0 started at 0 and ended at 1 with 1 unit of times.
Task 1 started at 1 and ended at 7 with 6 units of times.
Task 2 started at 7 and ended at 12 with 5 units of times.
Task 3 started at 12 and ended at 17 with 5 units of times.
The tasks with the longest time is task 1. The employee that worked on it is 3, so we return 3.
#### Example 3

- **Input:** $n = 2, logs = [[0,10],[1,20]]$
- **Output:** `0`
- **Explanation:**
Task 0 started at 0 and ended at 10 with 10 units of times.
Task 1 started at 10 and ended at 20 with 10 units of times.
The tasks with the longest time are tasks 0 and 1. The employees that worked on them are 0 and 1, so we return the smallest id 0.

### 4. Constraints

- $2 \le n \le 500$

- $1 \le \text{logs.length} \le 500$

- $\text{logs}[i].length = 2$

- $0 \le \text{id}_{i} \le n - 1$

- $1 \le \text{leaveTime}_{i} \le 500$

- $\text{id}_{i} \neq \text{id}_{i}+1$

- $\text{leaveTime}_{i}$ are sorted in a strictly increasing order.