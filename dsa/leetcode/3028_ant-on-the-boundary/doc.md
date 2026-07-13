# Ant on the Boundary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3028 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [ant-on-the-boundary](https://leetcode.com/problems/ant-on-the-boundary/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/ant-on-the-boundary/).

### Goal
An ant starts at the origin (position 0) on a 1D line. Given a sequence of moves represented by an array of integers, where positive values indicate movement to the right and negative values indicate movement to the left, determine how many times the ant returns to the origin (position 0) after completing each move.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence of moves.

**Return value**

- An integer representing the total count of times the ant lands back on 0 during its journey.

### Examples
**Example 1**

- Input: `nums = [2, 3, -5]`
- Output: `1`

**Example 2**

- Input: `nums = [3, 2, -3, -4]`
- Output: `0`

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a **Prefix Sum** approach. By maintaining a running total of the moves, we can track the ant's current position. Every time the running sum equals zero, we increment a counter.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only store the current position and the count of returns, requiring constant extra space.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    """
    Calculates the number of times an ant returns to the origin (0)
    given a sequence of moves.
    """
    current_position = 0
    return_count = 0

    for move in nums:
        current_position += move
        if current_position == 0:
            return_count += 1

    return return_count
```
</details>
