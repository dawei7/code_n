## Description

You are given an integer array `workers`, where `workers[i]` represents the skill level of the `i^th` worker. You are also given a 2D integer array `tasks`, where:

	- `tasks[i][0]` represents the skill requirement needed to complete the task.

	- `tasks[i][1]` represents the profit earned from completing the task.

Each worker can complete **at most** one task, and they can only take a task if their skill level is **equal** to the task's skill requirement. An **additional** worker joins today who can take up *any* task, **regardless** of the skill requirement.

Return the **maximum** total profit that can be earned by optimally assigning the tasks to the workers.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">workers = [1,2,3,4,5], tasks = [[1,100],[2,400],[3,100],[3,400]]</span>

**Output:** <span class="example-io">1000</span>

**Explanation:**

	- Worker 0 completes task 0.

	- Worker 1 completes task 1.

	- Worker 2 completes task 3.

	- The additional worker completes task 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">workers = [10,10000,100000000], tasks = [[1,100]]</span>

**Output:** <span class="example-io">100</span>

**Explanation:**

Since no worker matches the skill requirement, only the additional worker can complete task 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">workers = [7], tasks = [[3,3],[3,3]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The additional worker completes task 1. Worker 0 cannot work since no task has a skill requirement of 7.

</div>

**Constraints:**

	- `1 <= workers.length <= 10^5`

	- `1 <= workers[i] <= 10^9`

	- `1 <= tasks.length <= 10^5`

	- `tasks[i].length == 2`

	- `1 <= tasks[i][0], tasks[i][1] <= 10^9`
