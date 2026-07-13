# Find Minimum Cost to Remove Array Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3469 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-minimum-cost-to-remove-array-elements](https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/).

### Goal
Given an array of integers, you must remove all elements by repeatedly performing an operation: select two elements from the current array, remove them, and incur a cost equal to the maximum of the two values. The process continues until the array has either zero or one element remaining. If one element remains, it is removed at no additional cost. The objective is to minimize the total cost incurred across all operations.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array elements.

**Return value**

- An integer representing the minimum total cost to remove all elements from the array.

### Examples
**Example 1**

- Input: `nums = [6, 2, 8, 4]`
- Output: `12`
- Explanation: Remove (6, 8) cost 8, then (2, 4) cost 4. Total = 12.

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `2`
- Explanation: Remove (1, 1) cost 1, then (1, 1) cost 1. Total = 2.

**Example 3**

- Input: `nums = [1, 5, 6, 2]`
- Output: `8`
- Explanation: Remove (1, 5) cost 5, then (6, 2) cost 6. Total = 11. Wait, optimal is (1, 6) cost 6, (5, 2) cost 5 = 11. Actually, (5, 6) cost 6, (1, 2) cost 2 = 8.

---

## Solution
### Approach
The problem is solved using Dynamic Programming with memoization. Since we always remove two elements at a time, the state can be defined by the index of the first element currently being considered and the index of the "last remaining" element from the previous operation. We explore all valid pairings to find the minimum cost recursively.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the array, as there are `n^2` possible states in our memoization table.
- **Space Complexity**: `O(n^2)` to store the memoization table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    n = len(nums)
    states = {0: 0}
    index = 1

    while index + 1 < n:
        updated: dict[int, int] = {}
        first = nums[index]
        second = nums[index + 1]
        for leftover, cost in states.items():
            previous = nums[leftover]
            candidates = (
                (index + 1, cost + max(previous, first)),
                (index, cost + max(previous, second)),
                (leftover, cost + max(first, second)),
            )
            for next_leftover, next_cost in candidates:
                if next_cost < updated.get(next_leftover, 10**30):
                    updated[next_leftover] = next_cost
        states = updated
        index += 2

    if index == n:
        return min(cost + nums[leftover] for leftover, cost in states.items())
    return min(cost + max(nums[leftover], nums[index]) for leftover, cost in states.items())
```
</details>
