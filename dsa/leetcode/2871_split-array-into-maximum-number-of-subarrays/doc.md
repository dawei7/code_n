# Split Array Into Maximum Number of Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2871 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [split-array-into-maximum-number-of-subarrays](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/).

### Goal
Given an array of non-negative integers, partition the array into the maximum number of contiguous subarrays such that the bitwise AND of each subarray is equal to the minimum possible total bitwise AND of the entire array.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers (`List[int]`).

**Return value**

- An integer representing the maximum number of subarrays the array can be split into.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2, 0, 1, 2]`
- Output: `3`

**Example 2**

- Input: `nums = [5, 7, 1, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`

---

## Solution
### Approach
The problem relies on the property of the bitwise AND operation: the AND sum of a range is non-increasing as you include more elements. The minimum possible AND sum of the entire array is achieved by taking the AND of all elements in the array. If the total AND sum is greater than 0, the only possible split is the array itself (count = 1). If the total AND sum is 0, we can greedily partition the array whenever the running AND sum of a subarray reaches 0.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass to calculate the total AND and another pass to count the partitions.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the running AND sum and the partition count.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    # First, calculate the total bitwise AND of the entire array.
    # This represents the minimum possible AND sum for any partition.
    total_and = nums[0]
    for x in nums[1:]:
        total_and &= x

    # If the total AND is greater than 0, we cannot split the array into
    # multiple subarrays that each result in this same total_and.
    # Therefore, the maximum number of subarrays is 1.
    if total_and > 0:
        return 1

    # If the total AND is 0, we can greedily count how many subarrays
    # have an AND sum of 0.
    count = 0
    current_and = -1  # Initialize with all bits set

    for x in nums:
        if current_and == -1:
            current_and = x
        else:
            current_and &= x

        if current_and == 0:
            count += 1
            current_and = -1

    return count
```
</details>
