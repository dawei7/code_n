# Longest Subarray With Maximum Bitwise AND

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2419 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Brainteaser |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-subarray-with-maximum-bitwise-and](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/).

### Goal
Given an array of integers, identify the length of the longest contiguous subarray whose bitwise AND result is equal to the maximum possible bitwise AND value achievable by any subarray in the entire array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the length of the longest contiguous subarray that yields the maximum bitwise AND value.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 3, 2, 2]`
- Output: `2`
- Explanation: The maximum bitwise AND is 3. The longest subarray with this value is `[3, 3]`.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `1`
- Explanation: The maximum bitwise AND is 4. The longest subarray with this value is `[4]`.

**Example 3**

- Input: `nums = [7, 7, 7, 7]`
- Output: `4`
- Explanation: The maximum bitwise AND is 7. The entire array yields this value.

---

## Solution
### Approach
The key insight is that the bitwise AND of any subarray is always less than or equal to the maximum element in that subarray. Therefore, the maximum possible bitwise AND of any subarray is simply the maximum element present in the entire array. The problem reduces to finding the longest contiguous sequence of this maximum element.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass to find the maximum and another pass (or combined) to count the longest sequence.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the length of the longest contiguous subarray whose bitwise AND
    is equal to the maximum value in the array.
    """
    if not nums:
        return 0

    # The maximum bitwise AND of any subarray is the maximum element in the array.
    # This is because x & y <= min(x, y) <= max(x, y).
    max_val = max(nums)

    max_len = 0
    current_len = 0

    for x in nums:
        if x == max_val:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 0

    return max_len
```
</details>
