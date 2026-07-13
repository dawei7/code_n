# Count Ways to Group Overlapping Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2580 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-ways-to-group-overlapping-ranges](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/).

### Goal
Given a collection of closed intervals, determine the number of ways to partition these intervals into two distinct groups such that every interval in a group is connected to every other interval in the same group (either directly or transitively through overlapping intervals). Essentially, we are counting the number of disjoint connected components of intervals, where each component can be independently assigned to one of two groups. The result should be $2^k \pmod{10^9 + 7}$, where $k$ is the number of disjoint components.

### Function Contract
**Inputs**

- `ranges`: A list of lists, where each inner list `[start, end]` represents a closed interval.

**Return value**

- An integer representing the number of ways to group the intervals modulo $10^9 + 7$.

### Examples
**Example 1**

- Input: `ranges = [[6,10],[5,15]]`
- Output: `2`

**Example 2**

- Input: `ranges = [[1,3],[10,20],[2,5],[4,8]]`
- Output: `4`

**Example 3**

- Input: `ranges = [[1,2],[3,4]]`
- Output: `4`

---

## Solution
### Approach
The problem is solved by identifying connected components of intervals. By sorting the intervals based on their start times, we can perform a linear scan to merge overlapping intervals. If an interval starts after the end of the current merged range, it signifies the start of a new, independent component. The total number of ways is then $2^{\text{number of components}} \pmod{10^9 + 7}$.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of ranges, due to the initial sorting step. The subsequent linear scan takes $O(N)$.
- **Space Complexity**: $O(1)$ or $O(N)$ depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(ranges: list[list[int]]) -> int:
    MOD = 10**9 + 7

    # Sort ranges by start time
    ranges.sort()

    # Count the number of disjoint components
    components = 0
    if not ranges:
        return 0

    # Initialize with the first range
    current_end = -1

    for start, end in ranges:
        # If the current range starts after the previous merged end,
        # it's a new disjoint component.
        if start > current_end:
            components += 1
            current_end = end
        else:
            # Otherwise, merge the range by extending the current end
            current_end = max(current_end, end)

    # The result is 2^components % (10^9 + 7)
    return pow(2, components, MOD)
```
</details>
