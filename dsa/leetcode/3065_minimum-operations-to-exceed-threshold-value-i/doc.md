# Minimum Operations to Exceed Threshold Value I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3065 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-exceed-threshold-value-i](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/).

### Goal
Given a collection of integers and a target threshold, determine the minimum number of operations required to ensure that every element in the collection is at least as large as the threshold. An operation consists of removing any single element from the collection.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the current collection.
- `k`: An integer representing the minimum value threshold.

**Return value**

- An integer representing the count of elements that are strictly less than `k`.

### Examples
**Example 1**

- Input: `nums = [2, 11, 10, 1, 3]`, `k = 10`
- Output: `3`

**Example 2**

- Input: `nums = [1, 1, 2, 4, 9]`, `k = 1`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 2, 4, 9]`, `k = 9`
- Output: `4`

---

## Solution
### Approach
The problem is solved using a linear scan (filtering). We iterate through the array once and count how many elements fail to meet the condition `x >= k`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the input list, as we must inspect each element exactly once.
- **Space Complexity**: `O(1)`, as we only use a single counter variable regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the number of elements in nums that are strictly less than k.
    Removing these elements is the minimum operation to satisfy the threshold.
    """
    count = 0
    for num in nums:
        if num < k:
            count += 1
    return count
```
</details>
