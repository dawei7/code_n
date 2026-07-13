# Count Covered Buildings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3531 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-covered-buildings](https://leetcode.com/problems/count-covered-buildings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-covered-buildings/).

### Goal
Given a list of buildings represented by their start and end coordinates, determine how many buildings are "covered" by at least one other building. A building A is considered covered if there exists another building B such that the interval of A is entirely contained within the interval of B (i.e., `B.start <= A.start` and `A.end <= B.end`).

### Function Contract
**Inputs**

- `buildings`: A list of lists, where each sub-list `[start, end]` represents the inclusive range of a building.

**Return value**

- An integer representing the total count of buildings that are fully contained within the range of at least one other building.

### Examples
**Example 1**

- Input: `buildings = [[1,4],[3,6],[2,8]]`
- Output: `2`
- Explanation: [1,4] is covered by [2,8]. [3,6] is covered by [2,8].

**Example 2**

- Input: `buildings = [[1,4],[2,3]]`
- Output: `1`
- Explanation: [2,3] is covered by [1,4].

**Example 3**

- Input: `buildings = [[1,2],[3,4]]`
- Output: `0`
- Explanation: Neither building is contained within the other.

---

## Solution
### Approach
The problem is solved using a **Sorting and Sweep-line** approach. By sorting the buildings primarily by their start coordinates in ascending order and secondarily by their end coordinates in descending order, we can process buildings such that if a building `i` could potentially cover building `j`, it appears earlier in the sorted list. We then maintain the maximum end coordinate encountered so far to check if the current building's end coordinate is less than or equal to that maximum.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of buildings, due to the sorting step. The subsequent linear scan takes `O(N)`.
- **Space Complexity**: `O(1)` or `O(N)` depending on the sorting implementation's space requirements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(buildings: list[list[int]]) -> int:
    """
    Counts the number of buildings that are fully covered by another building.
    A building [s1, e1] is covered by [s2, e2] if s2 <= s1 and e1 <= e2.
    """
    if not buildings:
        return 0

    # Sort by start coordinate ascending.
    # If start coordinates are equal, sort by end coordinate descending.
    # This ensures that if a building covers another, the covering building
    # appears first in the list.
    buildings.sort(key=lambda x: (x[0], -x[1]))

    covered_count = 0
    max_end = -float('inf')

    for _, end in buildings:
        # If the current building's end is within the max_end seen so far,
        # it is covered by a previous building (since its start is >= previous start).
        if end <= max_end:
            covered_count += 1
        else:
            # Update the furthest end coordinate seen so far
            max_end = end

    return covered_count
```
</details>
