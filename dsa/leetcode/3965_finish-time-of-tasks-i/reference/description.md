### 1. Description

You are given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as a **tree** rooted at task 0. This is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates that task $u_{i}$ is the parent of task $v_{i}$.

You are also given an array `baseTime` of length `n`, where $\text{baseTime}[i]$ represents the time to complete task `i`.

The **finish time** of each task is calculated as follows:

- Leaf task: The finish time is $\text{baseTime}[i]$.

- Non-leaf task:

		<li>Let `earliest` be the **minimum** finish time among its children, and `latest` be the **maximum** finish time among its children.

- Let `ownDuration` be $(latest - earliest) + \text{baseTime}[i]$.

- The finish time of task `i` is $latest + ownDuration$.

	</li>

Return the finish time of the root task 0.

### 2. Function Contract

**Inputs**

- `n`: The number of tasks in the rooted tree.
- `edges`: The $n - 1$ directed parent-child pairs `[u, v]` that describe the tree rooted at `0`.
- `baseTime`: A list where $\text{baseTime}[i]$ is the positive base duration of task `i`.

**Return value**

Return the finish time of task `0` after applying the leaf and non-leaf rules recursively throughout the tree. The result is guaranteed to be exactly representable as an integer below $2^{53}$.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[1,2]], baseTime = [9,5,3]

**Output:** 17

**Explanation:**

<svg height="100" viewbox="0 0 420 140" width="300" xmlns="http://www.w3.org/2000/svg"> <rect fill="white" height="100%" width="100%"></rect> <line stroke="black" stroke-width="2" x1="80" x2="210" y1="60" y2="60"></line> <line stroke="black" stroke-width="2" x1="210" x2="340" y1="60" y2="60"></line> <circle cx="80" cy="60" fill="white" r="24" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="16" text-anchor="middle" x="80" y="65">0</text> <text fill="black" font-size="14" text-anchor="middle" x="80" y="100">9</text> <circle cx="210" cy="60" fill="white" r="24" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="16" text-anchor="middle" x="210" y="65">1</text> <text fill="black" font-size="14" text-anchor="middle" x="210" y="100">5</text> <circle cx="340" cy="60" fill="white" r="24" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="16" text-anchor="middle" x="340" y="65">2</text> <text fill="black" font-size="14" text-anchor="middle" x="340" y="100">3</text> </svg>

- Task 2 is a leaf, so its finish time is $\text{baseTime}[2] = 3$.

- Task 1 has one child task 2:

		<li>$earliest = latest = 3$

- $ownDuration = (latest - earliest) + \text{baseTime}[1] = 5$

- Finish time of task 1 is $3 + 5 = 8$

	</li>
- Task 0 has one child with finish time 8:

		<li>$earliest = latest = 8$

- $ownDuration = (latest - earliest) + \text{baseTime}[0] = 9$

- Finish time of task 0 is $8 + 9 = 17$

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[0,2]], baseTime = [4,7,6]

**Output:** 12

**Explanation:**

<svg height="130" viewbox="0 0 420 180" width="300" xmlns="http://www.w3.org/2000/svg"> <rect fill="white" height="100%" width="100%"></rect> <line stroke="black" stroke-width="2" x1="210" x2="110" y1="60" y2="130"></line> <line stroke="black" stroke-width="2" x1="210" x2="310" y1="60" y2="130"></line> <circle cx="210" cy="60" fill="white" r="24" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="16" text-anchor="middle" x="210" y="65">0</text> <text fill="black" font-size="14" text-anchor="middle" x="210" y="100">4</text> <circle cx="110" cy="130" fill="white" r="24" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="16" text-anchor="middle" x="110" y="135">1</text> <text fill="black" font-size="14" text-anchor="middle" x="110" y="170">7</text> <circle cx="310" cy="130" fill="white" r="24" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="16" text-anchor="middle" x="310" y="135">2</text> <text fill="black" font-size="14" text-anchor="middle" x="310" y="170">6</text> </svg>

- Task 1 is a leaf, so its finish time is $\text{baseTime}[1] = 7$.

- Task 2 is a leaf, so its finish time is $\text{baseTime}[2] = 6$.

- Task 0 has two children with finish times 7 and 6:

		<li>$earliest = 6$, $latest = 7$

- $ownDuration = (latest - earliest) + \text{baseTime}[0] = (7 - 6) + 4 = 5$

- Finish time of task 0 is $latest + ownDuration = 7 + 5 = 12$

	</li>

</div>
#### Example 3

<div class="example-block">
**Input:** n = 4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]

**Output:** 18

**Explanation:**

- Task 1 is a leaf, so its finish time is $\text{baseTime}[1] = 8$.

- Task 3 is a leaf, so its finish time is $\text{baseTime}[3] = 1$.

- Task 2 has one child task 3:

		<li>$earliest = latest = 1$

- $ownDuration = (latest - earliest) + \text{baseTime}[2] = 0 + 2 = 2$

- Finish time of task 2 is $latest + ownDuration = 1 + 2 = 3$

	</li>
- Task 0 has two children with finish times 8 and 3:

		<li>$earliest = 3$, $latest = 8$

- $ownDuration = (latest - earliest) + \text{baseTime}[0] = (8 - 3) + 5 = 10$

- Finish time of task 0 is $latest + ownDuration = 8 + 10 = 18$

	</li>

</div>

### 4. Constraints

- $1 \le n \le 10^{5}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i} \le n - 1$

- $u_{i} \neq v_{i}$

- The input is generated such that `edges` represents a valid tree.

- $\text{baseTime.length} = n$

- $1 \le \text{baseTime}[i] \le 10^{5}$​​​​​​​

- The finish time of every task is guaranteed to be less than $2^{53}$.