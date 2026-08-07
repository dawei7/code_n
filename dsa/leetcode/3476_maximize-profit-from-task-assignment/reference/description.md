### 1. Description

You are given an integer array `workers`, where $\text{workers}[i]$ represents the skill level of the $$i^{\text{th}}$$ worker. You are also given a 2D integer array `tasks`, where:

- $\text{tasks}[i][0]$ represents the skill requirement needed to complete the task.

- $\text{tasks}[i][1]$ represents the profit earned from completing the task.

Each worker can complete **at most** one task, and they can only take a task if their skill level is **equal** to the task's skill requirement. An **additional** worker joins today who can take up *any* task, **regardless** of the skill requirement.

Return the **maximum** total profit that can be earned by optimally assigning the tasks to the workers.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** workers = [1,2,3,4,5], tasks = [[1,100],[2,400],[3,100],[3,400]]

**Output:** 1000

**Explanation:**

- Worker 0 completes task 0.

- Worker 1 completes task 1.

- Worker 2 completes task 3.

- The additional worker completes task 2.

</div>
#### Example 2

<div class="example-block">
**Input:** workers = [10,10000,100000000], tasks = [[1,100]]

**Output:** 100

**Explanation:**

Since no worker matches the skill requirement, only the additional worker can complete task 0.

</div>
#### Example 3

<div class="example-block">
**Input:** workers = [7], tasks = [[3,3],[3,3]]

**Output:** 3

**Explanation:**

The additional worker completes task 1. Worker 0 cannot work since no task has a skill requirement of 7.

</div>

### 4. Constraints

- $1 \le \text{workers.length} \le 10^{5}$

- $1 \le \text{workers}[i] \le 10^{9}$

- $1 \le \text{tasks.length} \le 10^{5}$

- $\text{tasks}[i].length = 2$

- $1 \le \text{tasks}[i][0], \text{tasks}[i][1] \le 10^{9}$