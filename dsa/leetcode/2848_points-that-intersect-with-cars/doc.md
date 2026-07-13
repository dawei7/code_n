# Points That Intersect With Cars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2848 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [points-that-intersect-with-cars](https://leetcode.com/problems/points-that-intersect-with-cars/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/points-that-intersect-with-cars/).

### Goal
Given a list of intervals representing the range of coordinates occupied by various cars on a number line, determine the total number of unique integer coordinates that are covered by at least one car.

### Function Contract
**Inputs**

- `nums`: A list of lists, where each inner list `[start, end]` represents the inclusive range of coordinates covered by a car.

**Return value**

- An integer representing the count of distinct integer points covered by the union of all given intervals.

### Examples
**Example 1**

- Input: `nums = [[3,6],[1,5],[4,7]]`
- Output: `7`

**Example 2**

- Input: `nums = [[1,3],[5,8]]`
- Output: `6`

**Example 3**

- Input: `nums = [[1,2],[3,4],[5,6]]`
- Output: `6`

---

## Solution
### Approach
The problem can be solved using a **Set** to track unique integers or a **Difference Array/Prefix Sum** approach. Given the constraints (coordinates up to 100), a boolean array or a set is highly efficient. The set approach iterates through each interval, adds every integer in the range to a hash set, and returns the set's size.

### Complexity Analysis
- **Time Complexity**: `O(N * L)`, where `N` is the number of intervals and `L` is the average length of the intervals. In the worst case, this is bounded by the range of coordinates.
- **Space Complexity**: `O(M)`, where `M` is the total number of unique integer points covered, as we store them in a set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[List[int]]) -> int:
    """
    Calculates the number of unique integer points covered by a list of intervals.
    Uses a set to track unique coordinates.
    """
    covered_points = set()

    for start, end in nums:
        # Add all integers in the inclusive range [start, end] to the set
        for point in range(start, end + 1):
            covered_points.add(point)

    return len(covered_points)
```
</details>
