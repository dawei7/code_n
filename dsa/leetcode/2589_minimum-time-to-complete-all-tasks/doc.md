# Minimum Time to Complete All Tasks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2589 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Stack, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-complete-all-tasks](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/).

### Goal
Given a list of tasks where each task specifies a start time, an end time, and a required duration, determine the minimum number of time units (points) that must be active to satisfy all task requirements. A task is completed if it is active for its required duration within its specified [start, end] interval.

### Function Contract
**Inputs**

- `tasks`: A list of lists, where each inner list `[start, end, duration]` represents a task that must be completed within the inclusive range `[start, end]` for a total of `duration` time units.

**Return value**

- An integer representing the minimum number of time units that need to be marked as "active" to satisfy all task requirements.

### Examples
**Example 1**

- Input: `tasks = [[2,3,1],[4,5,1],[1,5,2]]`
- Output: `2`

**Example 2**

- Input: `tasks = [[1,3,2],[2,5,3],[5,6,2]]`
- Output: `4`

**Example 3**

- Input: `tasks = [[1,3,2],[4,9,3],[10,10,1]]`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a **Greedy approach with Sorting**. By sorting the tasks based on their end times, we can process tasks that finish earlier first. We maintain a boolean array (or a set of active time points) to track which time units are already "active." For each task, we count how many time units are already active within its interval. If the count is less than the required duration, we greedily fill the remaining required time units starting from the end of the interval moving backwards, as these points are most likely to be useful for subsequent tasks.

### Complexity Analysis
- **Time Complexity**: `O(N log N + N * M)`, where `N` is the number of tasks and `M` is the maximum end time. Sorting takes `O(N log N)`, and for each task, we iterate through its time range.
- **Space Complexity**: `O(M)`, where `M` is the maximum end time, used to store the status of each time unit.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(tasks: list[list[int]]) -> int:
    # Sort tasks by their end time to process them greedily
    tasks.sort(key=lambda x: x[1])

    # Find the maximum end time to determine the size of our timeline
    max_end = 0
    for task in tasks:
        if task[1] > max_end:
            max_end = task[1]

    # timeline[i] is True if time unit i is already marked as active
    timeline = [False] * (max_end + 1)

    for start, end, duration in tasks:
        # Count how many time units are already active in the current task's range
        active_count = 0
        for t in range(start, end + 1):
            if timeline[t]:
                active_count += 1

        # If we still need more time units, fill from the end backwards
        needed = duration - active_count
        if needed > 0:
            for t in range(end, start - 1, -1):
                if not timeline[t]:
                    timeline[t] = True
                    needed -= 1
                    if needed == 0:
                        break

    # The result is the total number of True values in the timeline
    return sum(timeline)
```
</details>
