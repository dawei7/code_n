# Happy Students

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2860 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [happy-students](https://leetcode.com/problems/happy-students/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/happy-students/).

### Goal
Determine the number of ways to select a group of students such that every student in the group is "happy." A student is happy if:
1. If the group size is $k$, and the student's requirement is $nums[i]$, then $nums[i] < k$ (if the student is selected).
2. If the student is not selected, their requirement $nums[i]$ must be greater than $k$.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the minimum number of students required to be present for each specific student to be happy.

**Return value**

- An integer representing the total number of valid ways to partition the students into a selected group and a non-selected group.

### Examples
**Example 1**

- Input: `nums = [1, 1]`
- Output: `2`
- Explanation: We can select 0 students (group size 0 < 1) or 2 students (group size 2 > 1).

**Example 2**

- Input: `nums = [1, 1, 0, 1]`
- Output: `4`
- Explanation: Valid group sizes are 0, 1, 3, and 4.

**Example 3**

- Input: `nums = [6, 0, 3, 3, 6, 7, 2, 7]`
- Output: `3`

---

## Solution
### Approach
The problem is solved by sorting the input array. Once sorted, we can iterate through all possible group sizes (from 0 to $n$). For a sorted array, if we choose a group size $k$, we are effectively selecting the first $k$ students. We then verify if the $k$-th student (if $k > 0$) has a requirement less than $k$, and if the $(k+1)$-th student (if $k < n$) has a requirement greater than $k$.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to the initial sorting of the array, where $n$ is the number of students. The subsequent linear scan takes $O(n)$.
- **Space Complexity**: $O(1)$ or $O(n)$ depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of ways to form a group of happy students.

    Args:
        nums: List of requirements for each student.

    Returns:
        The count of valid group sizes.
    """
    nums.sort()
    n = len(nums)
    count = 0

    # Case 1: Group size 0
    # Everyone is not selected. Requirement must be > 0.
    # Since nums is sorted, we only need to check the smallest element.
    if nums[0] > 0:
        count += 1

    # Case 2: Group size k (1 to n)
    # We select the first k students.
    # Condition: nums[k-1] < k AND (k == n OR nums[k] > k)
    for k in range(1, n + 1):
        if nums[k - 1] < k:
            if k == n or nums[k] > k:
                count += 1

    return count
```
</details>
