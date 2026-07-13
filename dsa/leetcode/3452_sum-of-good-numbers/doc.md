# Sum of Good Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3452 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-good-numbers](https://leetcode.com/problems/sum-of-good-numbers/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-good-numbers/).

### Goal
Given an array of integers and an integer `k`, identify all "good" numbers in the array. A number at index `i` is considered "good" if it is strictly greater than the elements at both index `i - k` and `i + k` (if those indices exist within the array bounds). The objective is to return the sum of all such good numbers.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the offset distance to check neighbors.

**Return value**

- An integer representing the sum of all elements that satisfy the "good" condition.

### Examples
**Example 1**

- Input: `nums = [1, 3, 2, 1, 5, 4], k = 2`
- Output: `12`
- Explanation: 3 is greater than 1 and 1 (indices 0 and 4), 5 is greater than 2 and 4 (indices 2 and 6 - wait, index 4 is 5, neighbors are 2 and 4). 3 + 5 + 4 = 12.

**Example 2**

- Input: `nums = [2, 1], k = 1`
- Output: `2`
- Explanation: 2 is greater than 1 (index 1).

**Example 3**

- Input: `nums = [3, 8, 6, 4, 1], k = 2`
- Output: `14`
- Explanation: 8 is greater than 3 and 4. 6 is greater than 8 (False). 6 is greater than 1. 8 + 6 = 14.

---

## Solution
### Approach
Linear scan (Iteration). The problem requires a single pass through the array to evaluate the condition for each element based on its relative neighbors at distance `k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a single variable to accumulate the sum.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the sum of all 'good' numbers in the array.
    A number is good if it is strictly greater than its neighbors at index i-k and i+k.
    """
    total_sum = 0
    n = len(nums)

    for i in range(n):
        is_good = True

        # Check left neighbor
        if i - k >= 0:
            if nums[i] <= nums[i - k]:
                is_good = False

        # Check right neighbor
        if i + k < n:
            if nums[i] <= nums[i + k]:
                is_good = False

        # If it passed both checks, add to sum
        if is_good:
            total_sum += nums[i]

    return total_sum
```
</details>
