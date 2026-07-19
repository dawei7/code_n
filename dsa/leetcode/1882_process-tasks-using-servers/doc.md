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
