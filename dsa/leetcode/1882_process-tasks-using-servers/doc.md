# Process Tasks Using Servers

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/process-tasks-using-servers/) |
| Frontend ID | 1882 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

There are $N$ indexed servers. `servers[i]` is server $i$'s weight, and all servers are initially free. The $j$-th task arrives at second $j$ and requires `tasks[j]` seconds of uninterrupted processing.

Waiting tasks remain in arrival order. Whenever both a waiting task and a free server exist, assign the oldest task to the free server with the smallest weight, breaking equal-weight ties by smaller server index. If no server is free, time advances until one or more finish; tasks are then assigned immediately under the same priorities. A task started at time $t$ releases its server at $t+\texttt{tasks[j]}$. Return the server index chosen for every task.

### Function Contract

**Inputs**

- `servers`: an array of $N$ positive server weights.
- `tasks`: an array of $M$ positive processing times; task $j$ arrives at second $j$.
- $1 \le N,M \le 2\cdot10^5$, and every weight and duration is at most $2\cdot10^5$.

**Return value**

- Return a length-$M$ array whose position $j$ is the index of the server assigned task $j$.

### Examples

**Example 1**

- Input: `servers = [3,3,2], tasks = [1,2,3,2,1,2]`
- Output: `[2,2,0,2,1,2]`

Server `2` has the smallest weight; the two weight-`3` servers tie by index.

**Example 2**

- Input: `servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]`
- Output: `[1,4,1,4,1,3,2]`

Several servers become free together at second `2`, after which weight priority applies again.

**Example 3**

- Input: `servers = [1], tasks = [5,1,1]`
- Output: `[0,0,0]`

Later tasks wait in order for the only server.

### Required Complexity

- **Time:** $O((N+M)\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Separate free and busy ordering**

Maintain an available min-heap of `(weight, index)`, exactly matching the choice rule for free servers. Maintain a busy min-heap of `(finish_time, weight, index)`. Its first field reveals the next scheduling event, while the remaining fields consistently order simultaneous releases.

**Process tasks in arrival order**

For task $j$, advance the simulated time to at least $j$ and move every server whose finish time is no later than that time into the available heap. If the available heap is nonempty, pop its best server and start the task immediately.

**Jump across a backlog**

If no server is available, jump time to the earliest busy finish. Release every server finishing then before choosing one; this is necessary because simultaneous finishers must compete by weight and index. Push the selected server back into the busy heap with finish time equal to the actual start time plus the task duration.

**Why this reproduces the queue**

Tasks are visited strictly by index, so no later arrival can pass an earlier waiting task. Before each assignment, all and only servers free at the current time have been transferred to the available heap. Its root is therefore precisely the server required by the tie rules. Each recorded assignment matches the specified event process by induction over tasks.

#### Complexity detail

Each of the $N$ servers enters the available heap initially. Across $M$ tasks, every assignment performs one removal and one busy insertion, and every completion causes at most one transfer back. Heap size never exceeds $N$, giving $O((N+M)\log N)$ time. The two heaps together store $N$ servers, so auxiliary space is $O(N)$. The required output occupies $O(M)$ additional result space.

#### Alternatives and edge cases

- **Scan all servers per task:** Tracking finish times in arrays is correct but selecting the best free server costs $O(NM)$ time.
- **One combined heap:** Availability time and weight have different priority orders, so a single static tuple order cannot represent both states safely.
- **Single server:** Every task receives index `0`, possibly after waiting.
- **Equal weights:** The smaller server index wins whenever both are free.
- **Simultaneous completions:** Release all servers at that time before assigning the next queued task.
- **Idle gaps:** When tasks arrive slower than completion, process each at its own arrival second.
- **Backlogged tasks:** Start time may be much larger than task index; use the simulated time, not the arrival, for the new finish time.

</details>
