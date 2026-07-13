# Process Tasks Using Servers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1882 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [process-tasks-using-servers](https://leetcode.com/problems/process-tasks-using-servers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/process-tasks-using-servers/).

### Goal
Assign tasks arriving one per second to servers. Free servers are chosen by smallest weight, then smallest index. Busy servers become available after finishing their assigned task.

### Function Contract
**Inputs**

- `servers`: server weights by index.
- `tasks`: task durations by arrival time.

**Return value**

Return the server index assigned to each task.

### Examples
**Example 1**

- Input: `servers = [3,3,2], tasks = [1,2,3,2,1,2]`
- Output: `[2,2,0,2,1,2]`

**Example 2**

- Input: `servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]`
- Output: `[1,4,1,4,1,3,2]`

**Example 3**

- Input: `servers = [1], tasks = [5,1,1]`
- Output: `[0,0,0]`

---

## Solution
### Approach
Maintain two heaps. The available heap stores `(weight, index)`. The busy heap stores `(finish_time, weight, index)`. At each task time, release every busy server whose finish time has arrived. If none is available, advance time to the earliest busy finish and release all servers available then. Assign the task to the best available server and push it into busy with its finish time.

### Complexity Analysis
- **Time Complexity**: `O((n + m) log n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
