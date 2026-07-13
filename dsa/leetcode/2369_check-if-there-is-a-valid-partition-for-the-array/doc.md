# Check if There is a Valid Partition For The Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2369 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-there-is-a-valid-partition-for-the-array](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/).

### Goal
Determine if an integer array can be partitioned into one or more contiguous subarrays, where each subarray must satisfy one of three specific conditions: it contains two equal elements, three equal elements, or three consecutive increasing elements (with a difference of 1).

### Function Contract
**Inputs**

- `nums`: A list of integers where 0 <= nums[i] <= 10^6.

**Return value**

- A boolean indicating whether a valid partition of the entire array exists.

### Examples
**Example 1**

- Input: `nums = [4,4,4,5,6]`
- Output: `true`
- Explanation: The array can be partitioned into [4,4] and [4,5,6].

**Example 2**

- Input: `nums = [1,1,1,2]`
- Output: `false`
- Explanation: No valid partition exists for the given array.

**Example 3**

- Input: `nums = [3,3,3]`
- Output: `true`
- Explanation: The array can be partitioned into [3,3,3].

---

## Solution
### Approach
Dynamic Programming (Bottom-Up). We maintain a boolean array `dp` where `dp[i]` represents whether the prefix of the array of length `i` can be validly partitioned. The state transition checks if the last 2 or 3 elements satisfy the required conditions and if the preceding prefix was also valid.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the array once.
- **Space Complexity**: O(n) to store the DP table (can be optimized to O(1) by only keeping track of the last three states).

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> bool:
    n = len(nums)
    # dp[i] will be True if the prefix of length i is validly partitionable
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(2, n + 1):
        # Check for 2 equal elements
        if i >= 2:
            if nums[i-1] == nums[i-2]:
                if dp[i-2]:
                    dp[i] = True

        # Check for 3 equal elements or 3 consecutive increasing elements
        if i >= 3:
            # 3 equal elements
            if nums[i-1] == nums[i-2] == nums[i-3]:
                if dp[i-3]:
                    dp[i] = True
            # 3 consecutive increasing elements
            elif nums[i-1] == nums[i-2] + 1 == nums[i-3] + 2:
                if dp[i-3]:
                    dp[i] = True

    return dp[n]
```
</details>
