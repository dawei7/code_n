# The Employee That Worked on the Longest Task

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2432 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [the-employee-that-worked-on-the-longest-task](https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/).

### Goal
Given a sequence of tasks performed by employees, where each task is defined by an employee ID and the time at which the task was completed, determine which employee spent the longest duration on a single task. If multiple employees share the same maximum duration, return the smallest employee ID among them.

### Function Contract
**Inputs**

- `n`: An integer representing the total number of employees (IDs range from 0 to n-1).
- `logs`: A list of lists, where each inner list `[id, leaveTime]` indicates that employee `id` finished their task at `leaveTime`.

**Return value**

- An integer representing the ID of the employee who completed the longest task.

### Examples
**Example 1**

- Input: `n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]`
- Output: `1`

**Example 2**

- Input: `n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]`
- Output: `3`

**Example 3**

- Input: `n = 2, logs = [[0,10],[1,20]]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a single-pass linear scan. We maintain the `max_duration` found so far and the corresponding `employee_id`. By calculating the difference between the current task's completion time and the previous task's completion time, we determine the duration of the current task. We update the result if the current duration is strictly greater than the `max_duration`, or if it is equal but the current `employee_id` is smaller.

### Complexity Analysis
- **Time Complexity**: `O(L)`, where `L` is the number of logs, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store a few variables to track the maximum duration and the best employee ID found so far.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, logs: list[list[int]]) -> int:
    max_duration = -1
    result_id = -1
    prev_time = 0

    for emp_id, end_time in logs:
        duration = end_time - prev_time

        if duration > max_duration:
            max_duration = duration
            result_id = emp_id
        elif duration == max_duration:
            if emp_id < result_id:
                result_id = emp_id

        prev_time = end_time

    return result_id
```
</details>
