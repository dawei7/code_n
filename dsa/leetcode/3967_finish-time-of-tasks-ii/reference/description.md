## Description

You are given an integer `n` representing the number of tasks in a project, numbered from 0 to $n - 1$. These tasks are connected as an undirected** tree**. This is represented by a 2D integer array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an undirected connection between task $u_{i}$ and task $v_{i}$.

You are also given an array `baseTime` of length `n`, where $\text{baseTime}[i]$ represents the time to complete task `i`.

For any chosen task as the root, the **finish time** of each task is calculated as follows:

- Leaf task: The finish time is $\text{baseTime}[i]$.

- Non-leaf task:

		<li>Let `earliest` be the **minimum** finish time among its children, and `latest` be the **maximum** finish time among its children.

- Let `ownDuration` be $(latest - earliest) + \text{baseTime}[i]$.

- Finish time of task `i` is $latest + ownDuration$.

	</li>

Choose **any** task as the root and compute the finish time of that root based on the rules above.

Return the **minimum** possible finish time among all choices of root.
### Function Contract

**Inputs**

- `n`: The number of tasks in the project.
- `edges`: The `n - 1` undirected pairs `[u, v]` that form a valid tree over tasks `0` through `n - 1`.
- `baseTime`: A list where `baseTime[i]` is the positive base completion time of task `i`.

**Return value**

Return the minimum possible finish time of the chosen root after orienting the tree away from that root and applying the leaf and non-leaf finish-time rules recursively.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[1,2]], baseTime = [9,1,5]

**Output:** 14

**Explanation:**

<svg height="110" viewbox="50 30 400 124" width="350" xmlns="http://www.w3.org/2000/svg"> <rect fill="white" height="124" width="400" x="50" y="30"></rect> <line stroke="black" stroke-width="2" x1="100" x2="250" y1="80" y2="80"></line> <line stroke="black" stroke-width="2" x1="250" x2="400" y1="80" y2="80"></line> <circle cx="100" cy="80" fill="white" r="30" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="100" y="87">0</text> <text fill="black" font-size="16" text-anchor="middle" x="100" y="131">9</text> <circle cx="250" cy="80" fill="white" r="30" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="250" y="87">1</text> <text fill="black" font-size="16" text-anchor="middle" x="250" y="131">1</text> <circle cx="400" cy="80" fill="white" r="30" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="400" y="87">2</text> <text fill="black" font-size="16" text-anchor="middle" x="400" y="131">5</text> </svg>

The optimal choice is to treat task 1 as the root.

- Task 0 is a leaf, so its finish time is $\text{baseTime}[0] = 9$.

- Task 2 is a leaf, so its finish time is $\text{baseTime}[2] = 5$.

- Task 1 has two children with finish times 9 and 5:

		<li>$earliest = 5$, $latest = 9$

- $ownDuration = (latest - earliest) + \text{baseTime}[1] = (9 - 5) + 1 = 5$

- Finish time of task 1 is $latest + ownDuration = 9 + 5 = 14$

	</li>

Thus, the minimum possible finish time among all choices of root is 14.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[0,2]], baseTime = [4,7,6]

**Output:** 12

**Explanation:**

<svg height="215" viewbox="48 14 324 232" width="300" xmlns="http://www.w3.org/2000/svg"> <rect fill="white" height="232" width="324" x="48" y="14"></rect> <line stroke="black" stroke-width="2" x1="210" x2="110" y1="60" y2="180"></line> <line stroke="black" stroke-width="2" x1="210" x2="310" y1="60" y2="180"></line> <circle cx="210" cy="60" fill="white" r="32" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="210" y="66">0</text> <text fill="black" font-size="16" text-anchor="middle" x="210" y="110">4</text> <circle cx="110" cy="180" fill="white" r="32" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="110" y="186">1</text> <text fill="black" font-size="16" text-anchor="middle" x="110" y="230">7</text> <circle cx="310" cy="180" fill="white" r="32" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="310" y="186">2</text> <text fill="black" font-size="16" text-anchor="middle" x="310" y="230">6</text> </svg>

The optimal choice is to treat task 0 as the root.

- Task 1 is a leaf, so its finish time is $\text{baseTime}[1] = 7$.

- Task 2 is a leaf, so its finish time is $\text{baseTime}[2] = 6$.

- Task 0 has two children with finish times 7 and 6:

		<li>$earliest = 6$, $latest = 7$

- $ownDuration = (latest - earliest) + \text{baseTime}[0] = (7 - 6) + 4 = 5$

- Finish time of task 0 is $latest + ownDuration = 7 + 5 = 12$

	</li>

Thus, the minimum possible finish time among all choices of root is 12.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]

**Output:** 16

**Explanation:**

<svg height="368" viewbox="46 26 380 466" width="300" xmlns="http://www.w3.org/2000/svg"> <rect fill="white" height="466" width="380" x="46" y="26"></rect> <line stroke="black" stroke-width="2" x1="230" x2="110" y1="80" y2="260"></line> <line stroke="black" stroke-width="2" x1="230" x2="350" y1="80" y2="260"></line> <line stroke="black" stroke-width="2" x1="350" x2="350" y1="260" y2="420"></line> <circle cx="230" cy="80" fill="white" r="34" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="230" y="88">0</text> <text fill="black" font-size="16" text-anchor="middle" x="230" y="132">5</text> <circle cx="110" cy="260" fill="white" r="34" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="110" y="268">1</text> <text fill="black" font-size="16" text-anchor="middle" x="110" y="312">8</text> <circle cx="350" cy="260" fill="white" r="34" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="350" y="268">2</text> <text fill="black" font-size="16" text-anchor="middle" x="398" y="266">2</text> <circle cx="350" cy="420" fill="white" r="34" stroke="black" stroke-width="2"></circle> <text fill="black" font-size="18" text-anchor="middle" x="350" y="428">3</text> <text fill="black" font-size="16" text-anchor="middle" x="350" y="472">1</text> </svg>

The optimal choice is to treat task 1 as the root.

- Task 3 is a leaf, so its finish time is $\text{baseTime}[3] = 1$.

- Task 2 has one child task 3:

		<li>$earliest = latest = 1$

- $ownDuration = (latest - earliest) + \text{baseTime}[2] = 0 + 2 = 2$

- Finish time of task 2 is $latest + ownDuration = 1 + 2 = 3$

	</li>
- Task 0 has one child task 2:

		<li>$earliest = latest = 3$

- $ownDuration = (latest - earliest) + \text{baseTime}[0] = 0 + 5 = 5$

- Finish time of task 0 is $latest + ownDuration = 3 + 5 = 8$

	</li>
- Task 1 has one child task 0:

		<li>$earliest = latest = 8$

- $ownDuration = (latest - earliest) + \text{baseTime}[1] = 0 + 8 = 8$

- Finish time of task 1 is $latest + ownDuration = 8 + 8 = 16$

	</li>

Thus, the minimum possible finish time among all choices of root is 16.

</div>
### Constraints

- $1 \le n \le 10^{5}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i} \le n - 1$

- $u_{i} \neq v_{i}$

- The input is generated such that `edges` represents a valid undirected tree.

- $\text{baseTime.length} = n$

- $1 \le \text{baseTime}[i] \le 10^{5}$