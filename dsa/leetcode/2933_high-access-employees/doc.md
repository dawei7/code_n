# High-Access Employees

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2933 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [high-access-employees](https://leetcode.com/problems/high-access-employees/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/high-access-employees/).

### Goal
Identify "high-access" employees who have accessed a secure system at least three times within a single one-hour window. Access times are provided in 24-hour HHMM format. An employee is considered high-access if there exist three timestamps $t_1, t_2, t_3$ for that employee such that they all fall within a range of strictly less than 60 minutes.

### Function Contract
**Inputs**

- `access_times`: A list of lists, where each inner list contains two strings: the employee name and their access time in "HHMM" format.

**Return value**

- A list of strings representing the names of all high-access employees, sorted in any order.

### Examples
**Example 1**

- Input: `access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0615"],["a","0559"]]`
- Output: `["a"]`

**Example 2**

- Input: `access_times = [["d","0002"],["c","0808"],["c","0809"],["c","0810"]]`
- Output: `["c"]`

**Example 3**

- Input: `access_times = [["cd","1025"],["ig","1025"],["cd","1026"],["cd","1027"],["ig","1028"],["ig","1029"]]`
- Output: `["cd","ig"]`

---

## Solution
### Approach
The solution utilizes a Hash Map (dictionary) to group access times by employee. For each employee, the access times are converted into integer minutes from the start of the day and sorted. A sliding window approach (or checking index `i` and `i+2`) is then used to determine if any three timestamps fall within a 60-minute interval.

### Complexity Analysis
- **Time Complexity**: $O(N \log N + N \cdot K \log K)$, where $N$ is the number of access records and $K$ is the average number of access records per employee. Sorting the records per employee dominates the complexity.
- **Space Complexity**: $O(N)$, required to store the grouped access times in the hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(access_times: list[list[str]]) -> list[str]:
    # Group access times by employee
    employee_map = defaultdict(list)
    for name, time_str in access_times:
        # Convert HHMM to total minutes from start of day
        hours = int(time_str[:2])
        minutes = int(time_str[2:])
        total_minutes = hours * 60 + minutes
        employee_map[name].append(total_minutes)

    high_access_employees = []

    for name, times in employee_map.items():
        # We need at least 3 accesses to qualify
        if len(times) < 3:
            continue

        # Sort times to check sliding window
        times.sort()

        # Check if any 3 accesses occur within a 60-minute window
        # If times[i+2] - times[i] < 60, then times[i], times[i+1], times[i+2]
        # are all within a 60-minute range.
        for i in range(len(times) - 2):
            if times[i + 2] - times[i] < 60:
                high_access_employees.append(name)
                break

    return high_access_employees
```
</details>
