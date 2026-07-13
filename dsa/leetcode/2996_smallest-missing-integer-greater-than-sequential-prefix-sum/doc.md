# Smallest Missing Integer Greater Than Sequential Prefix Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2996 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-missing-integer-greater-than-sequential-prefix-sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/).

### Goal
Given an array of integers, identify the longest prefix that consists of consecutive integers (where each element is exactly one greater than the previous). Calculate the sum of this prefix. Then, find the smallest integer greater than or equal to this sum that is not present anywhere in the original array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the smallest missing value that is at least as large as the calculated prefix sum.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 2, 5]`
- Output: `6`
- Explanation: The longest sequential prefix is `[1, 2, 3]`, sum = 6. 6 is not in the array, so return 6.

**Example 2**

- Input: `nums = [3, 4, 5, 1, 12, 14, 13]`
- Output: `15`
- Explanation: The longest sequential prefix is `[3, 4, 5]`, sum = 12. 12 is in the array, 13 is in the array, 14 is in the array, but 15 is not.

**Example 3**

- Input: `nums = [2, 3, 1]`
- Output: `2`
- Explanation: The longest sequential prefix is `[2]`, sum = 2. 2 is in the array, 3 is in the array, but 4 is not. Wait, the prefix is `[2]`, sum is 2. 2 is in the array, 3 is in the array, 4 is not.

---

## Solution
### Approach
The algorithm utilizes a linear scan to determine the sequential prefix sum, followed by a hash set lookup to efficiently check for the existence of integers starting from that sum.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array. We iterate through the array once to find the prefix sum and once to populate the hash set.
- **Space Complexity**: `O(n)` to store the elements of the array in a hash set for O(1) average time complexity lookups.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    # Calculate the sum of the longest sequential prefix
    prefix_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
        else:
            break

    # Use a set for O(1) average time complexity lookups
    num_set = set(nums)

    # Find the smallest integer >= prefix_sum not in the set
    current = prefix_sum
    while current in num_set:
        current += 1

    return current
```
</details>
