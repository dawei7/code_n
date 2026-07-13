# Minimum Processing Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2895 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-processing-time](https://leetcode.com/problems/minimum-processing-time/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-processing-time/).

### Goal
Given a list of processor start times and a list of tasks with varying execution durations, assign each processor exactly four tasks. The goal is to minimize the total time required to complete all tasks, where the completion time for a specific processor is defined as its start time plus the duration of the longest task assigned to it. The total time is the maximum completion time among all processors.

### Function Contract
**Inputs**

- `processorTime`: A list of integers representing the time at which each processor becomes available.
- `tasks`: A list of integers representing the duration of each task.

**Return value**

- An integer representing the minimum possible time required to finish all tasks.

### Examples
**Example 1**

- Input: `processorTime = [8, 10]`, `tasks = [2, 2, 3, 1, 8, 7, 4, 5]`
- Output: `16`

**Example 2**

- Input: `processorTime = [10, 20]`, `tasks = [2, 3, 1, 2, 5, 8, 4, 3]`
- Output: `23`

**Example 3**

- Input: `processorTime = [1, 5]`, `tasks = [1, 1, 1, 1, 1, 1, 1, 1]`
- Output: `6`

---

## Solution
### Approach
The problem is solved using a **Greedy Strategy**. To minimize the maximum completion time, we should pair the processors that become available latest with the tasks that take the longest time. By sorting the `processorTime` in descending order and the `tasks` in ascending order, we can greedily assign the four largest tasks to the processor that starts latest, the next four largest to the next latest, and so on.

### Complexity Analysis
- **Time Complexity**: `O(N log N + M log M)`, where `N` is the number of processors and `M` is the number of tasks. This is dominated by the sorting of both input arrays.
- **Space Complexity**: `O(1)` or `O(N + M)` depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(processorTime: List[int], tasks: List[int]) -> int:
    """
    Calculates the minimum time to complete all tasks by greedily pairing
    the latest available processors with the longest tasks.
    """
    # Pair the earliest processors with the largest tasks, leaving smaller
    # batches for processors that start later.
    processorTime.sort()

    # Sort tasks in ascending order.
    tasks.sort()

    max_completion_time = 0

    # Each processor handles 4 tasks.
    # We iterate through processors and pick the 4 largest remaining tasks.
    # Since tasks are sorted ascending, the largest tasks are at the end.
    task_idx = len(tasks) - 1

    for p_time in processorTime:
        # The current processor takes the 4 largest available tasks.
        # The time taken by this processor is p_time + max(assigned_tasks).
        # Because tasks are sorted, the largest task in this batch is at task_idx.
        current_processor_finish = p_time + tasks[task_idx]

        if current_processor_finish > max_completion_time:
            max_completion_time = current_processor_finish

        # Move to the next 4 largest tasks
        task_idx -= 4

    return max_completion_time
```
</details>
