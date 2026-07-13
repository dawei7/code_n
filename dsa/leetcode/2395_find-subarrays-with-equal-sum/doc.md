# Find Subarrays With Equal Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2395 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-subarrays-with-equal-sum](https://leetcode.com/problems/find-subarrays-with-equal-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-subarrays-with-equal-sum/).

### Goal
Determine if an integer array contains at least two distinct subarrays of length two that result in the same sum. A subarray is defined as a contiguous sequence of elements within the array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- `bool`: Returns `True` if there exist two different starting indices `i` and `j` (where `i != j`) such that `nums[i] + nums[i+1] == nums[j] + nums[j+1]`, otherwise returns `False`.

### Examples
**Example 1**

- Input: `nums = [4, 2, 4]`
- Output: `True`
- Explanation: The subarray [4, 2] sums to 6, and [2, 4] sums to 6.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `False`
- Explanation: No two subarrays of length two have the same sum.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `True`
- Explanation: The subarrays [0, 0] at indices 0 and 1 both sum to 0.

---

## Solution
### Approach
The problem is solved using a **Hash Set** to track the sums of all encountered subarrays of length two. By iterating through the array once and calculating the sum of adjacent pairs, we can check for existence in $O(1)$ average time.

### Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the input array, as we perform a single pass over the array.
- **Space Complexity**: $O(n)$, as in the worst case, we store up to $n-1$ unique sums in the hash set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if there are two subarrays of length 2 with the same sum.
    """
    seen_sums = set()

    # Iterate through the array to calculate sums of adjacent pairs
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        # If the sum has been seen before, we found a duplicate
        if current_sum in seen_sums:
            return True

        # Otherwise, add the sum to our set
        seen_sums.add(current_sum)

    return False
```
</details>
