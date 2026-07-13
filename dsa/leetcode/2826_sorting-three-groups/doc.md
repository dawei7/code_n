# Sorting Three Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2826 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sorting-three-groups](https://leetcode.com/problems/sorting-three-groups/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sorting-three-groups/).

### Goal
Given an array of integers where each element is either 1, 2, or 3, determine the minimum number of elements that must be moved (or changed) to make the entire array non-decreasing. Since we only care about the relative order of 1s, 2s, and 3s, this is equivalent to finding the Longest Non-Decreasing Subsequence of the array and subtracting its length from the total number of elements.

### Function Contract
**Inputs**

- `nums`: A list of integers where each integer is 1, 2, or 3.

**Return value**

- An integer representing the minimum number of operations required to sort the array in non-decreasing order.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 2, 1]`
- Output: `3`

**Example 2**

- Input: `nums = [1, 3, 2, 1, 3, 3]`
- Output: `2`

**Example 3**

- Input: `nums = [2, 2, 2, 2, 3, 3]`
- Output: `0`

---

## Solution
### Approach
Dynamic Programming. We maintain the state of the minimum operations required to end in a non-decreasing sequence ending with a 1, 2, or 3. Alternatively, this can be solved by finding the Longest Non-Decreasing Subsequence (LNDS) using the property that the sequence must consist of a block of 1s, followed by a block of 2s, followed by a block of 3s.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array once.
- **Space Complexity**: `O(1)`, as we only store the counts for the three possible ending states.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    To make the array non-decreasing, we want to keep the longest subsequence
    that is already in the form 1...1, 2...2, 3...3.

    Let dp[i] be the minimum operations to make the prefix of the array
    sorted such that the last element is of type i (where i is 1, 2, or 3).

    - If current is 1:
        dp[1] = dp[1]
        dp[2] = dp[2] + 1
        dp[3] = dp[3] + 1
    - If current is 2:
        dp[1] = dp[1] + 1
        dp[2] = min(dp[1], dp[2])
        dp[3] = dp[3] + 1
    - If current is 3:
        dp[1] = dp[1] + 1
        dp[2] = dp[2] + 1
        dp[3] = min(dp[1], dp[2], dp[3])
    """
    # dp[i] stores the min operations to have a sorted sequence ending in value (i+1)
    dp = [0, 0, 0]

    for x in nums:
        if x == 1:
            # To end in 1: no change needed
            # To end in 2: must change 1 to 2
            # To end in 3: must change 1 to 3
            dp[0] = dp[0]
            dp[1] = dp[1] + 1
            dp[2] = dp[2] + 1
        elif x == 2:
            # To end in 1: must change 2 to 1
            # To end in 2: min of ending in 1 or 2
            # To end in 3: must change 2 to 3
            dp[0] = dp[0] + 1
            dp[1] = min(dp[0] - 1, dp[1])
            dp[2] = dp[2] + 1
        else: # x == 3
            # To end in 1: must change 3 to 1
            # To end in 2: must change 3 to 2
            # To end in 3: min of ending in 1, 2, or 3
            dp[0] = dp[0] + 1
            dp[1] = dp[1] + 1
            dp[2] = min(dp[0] - 1, dp[1] - 1, dp[2])

    return min(dp)
```
</details>
