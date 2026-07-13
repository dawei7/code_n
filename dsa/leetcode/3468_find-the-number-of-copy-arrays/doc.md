# Find the Number of Copy Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3468 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-copy-arrays](https://leetcode.com/problems/find-the-number-of-copy-arrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-copy-arrays/).

### Goal
Given an original array `original` and a list of constraints `bounds` where each element `bounds[i]` specifies a range `[min_i, max_i]` for the `i`-th element of a new array `copy`, determine how many distinct arrays `copy` can be formed such that the difference between consecutive elements in `copy` is identical to the difference between consecutive elements in `original`.

### Function Contract
**Inputs**

- `original`: A list of integers representing the base sequence.
- `bounds`: A list of lists, where each `bounds[i]` contains two integers `[min_i, max_i]` representing the inclusive range for the `i`-th element of the resulting array.

**Return value**

- An integer representing the total number of valid arrays that satisfy the difference constraints and the range bounds.

### Examples
**Example 1**

- Input: `original = [1, 2, 3]`, `bounds = [[1, 2], [2, 3], [3, 4]]`
- Output: `1`

**Example 2**

- Input: `original = [1, 2, 3]`, `bounds = [[1, 2], [1, 2], [1, 2]]`
- Output: `0`

**Example 3**

- Input: `original = [1, 1, 1]`, `bounds = [[1, 10], [2, 9]]`
- Output: `8`

---

## Solution
### Approach
The problem is solved using a greedy range-tracking approach. Since the difference between consecutive elements is fixed by the `original` array, if we choose a value `x` for the first element, all subsequent elements are determined by `copy[i] = copy[i-1] + (original[i] - original[i-1])`. This implies that for each index `i`, the value `copy[i]` must fall within `[bounds[i][0], bounds[i][1]]`. By shifting these bounds relative to the first element, we can find the intersection of all valid ranges for the first element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the `original` array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only store the current valid range boundaries.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(original: List[int], bounds: List[List[int]]) -> int:
    # The difference between consecutive elements in the copy array
    # must match the difference in the original array.
    # Let diff[i] = original[i] - original[i-1].
    # Then copy[i] = copy[0] + sum(diff[1...i]).
    # Let S[i] = sum(diff[1...i]) with S[0] = 0.
    # Then copy[i] = copy[0] + S[i].
    # The constraint is: bounds[i][0] <= copy[0] + S[i] <= bounds[i][1]
    # Which rearranges to: bounds[i][0] - S[i] <= copy[0] <= bounds[i][1] - S[i]

    current_min = bounds[0][0]
    current_max = bounds[0][1]

    cumulative_diff = 0
    for i in range(1, len(original)):
        cumulative_diff += (original[i] - original[i-1])

        # Update the valid range for copy[0] based on the current index constraint
        # copy[0] must be >= bounds[i][0] - cumulative_diff
        # copy[0] must be <= bounds[i][1] - cumulative_diff
        current_min = max(current_min, bounds[i][0] - cumulative_diff)
        current_max = min(current_max, bounds[i][1] - cumulative_diff)

    if current_min > current_max:
        return 0

    return current_max - current_min + 1
```
</details>
