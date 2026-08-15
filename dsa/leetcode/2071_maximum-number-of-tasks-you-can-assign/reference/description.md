### 1. Description

You have `n` tasks and `m` workers. Each task has a strength requirement stored in a **0-indexed** integer array `tasks`, with the $$i^{\text{th}}$$ task requiring $\text{tasks}[i]$ strength to complete. The strength of each worker is stored in a **0-indexed** integer array `workers`, with the $$j^{\text{th}}$$ worker having $\text{workers}[j]$ strength. Each worker can only be assigned to a **single** task and must have a strength **greater than or equal** to the task's strength requirement (i.e., $\text{workers}[j] \ge \text{tasks}[i]$).

Additionally, you have `pills` magical pills that will **increase a worker's strength** by `strength`. You can decide which workers receive the magical pills, however, you may only give each worker **at most one** magical pill.

Given the **0-indexed **integer arrays `tasks` and `workers` and the integers `pills` and `strength`, return *the **maximum** number of tasks that can be completed.*

### 2. Function Contract

**Inputs**

- `tasks`: Input parameter (`List[int]`).
- `workers`: Input parameter (`List[int]`).
- `pills`: Input parameter (`int`).
- `strength`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $tasks = [<u>**3**</u>,<u>**2**</u>,<u>**1**</u>], workers = [<u>**0**</u>,<u>**3**</u>,<u>**3**</u>], pills = 1, strength = 1$
- **Output:** `3`
- **Explanation:** We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

#### Example 2

- **Input:** $tasks = [<u>**5**</u>,4], workers = [<u>**0**</u>,0,0], pills = 1, strength = 5$
- **Output:** `1`
- **Explanation:** We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

#### Example 3

- **Input:** $tasks = [<u>**10**</u>,<u>**15**</u>,30], workers = [<u>**0**</u>,<u>**10**</u>,10,10,10], pills = 3, strength = 10$
- **Output:** `2`
- **Explanation:** We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

### 4. Constraints

- $n = \text{tasks.length}$

- $m = \text{workers.length}$

- $1 \le n, m \le 5 * 10^{4}$

- $0 \le pills \le m$

- $0 \le \text{tasks}[i], \text{workers}[j], strength \le 10^{9}$
