# Minimum Operations to Collect Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2869 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-operations-to-collect-elements](https://leetcode.com/problems/minimum-operations-to-collect-elements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-operations-to-collect-elements/).

### Goal
Given an array of integers and an integer `k`, determine the minimum number of elements that must be removed from the end of the array to collect all integers from 1 to `k` inclusive.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence.
- `k`: An integer representing the target range of values [1, k] to collect.

**Return value**

- An integer representing the minimum number of operations (removals from the end) required to gather all integers in the set {1, 2, ..., k}.

### Examples
**Example 1**

- Input: `nums = [3, 1, 5, 4, 2], k = 2`
- Output: `4`
- Explanation: Removing 2, 4, 5, 1 leaves {3, 1}. We have collected 1 and 2.

**Example 2**

- Input: `nums = [3, 1, 5, 4, 2], k = 5`
- Output: `5`

**Example 3**

- Input: `nums = [3, 2, 5, 3, 1], k = 3`
- Output: `4`

---

## Solution
### Approach
The problem is solved using a reverse iteration approach combined with a Hash Set (or a boolean array) to track unique collected elements. By traversing the array from right to left, we can greedily identify the first occurrence of each number in the range [1, k]. Once the size of our tracking set reaches `k`, the current index provides the total count of operations.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we traverse the array at most once.
- **Space Complexity**: `O(k)`, as we store at most `k` unique integers in our tracking set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to collect all integers from 1 to k
    by iterating backwards through the list.
    """
    collected = set()
    operations = 0

    # Iterate backwards through the array
    for i in range(len(nums) - 1, -1, -1):
        operations += 1
        val = nums[i]

        # Only track values within the target range [1, k]
        if val <= k:
            collected.add(val)

        # If we have collected all numbers from 1 to k, return the count
        if len(collected) == k:
            return operations

    return operations
```
</details>
