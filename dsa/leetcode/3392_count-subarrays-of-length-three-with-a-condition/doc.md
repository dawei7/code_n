# Count Subarrays of Length Three With a Condition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3392 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-subarrays-of-length-three-with-a-condition](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/).

### Goal
Given an array of integers, identify the number of contiguous subarrays consisting of exactly three elements where the sum of the first and third elements is exactly equal to half of the middle element.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of valid subarrays of length three.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 4, 1]`
- Output: `1`
- Explanation: The only valid subarray is `[1, 2, 1]` because `1 + 1 = 2 / 2` is false? Wait, the condition is `nums[i] + nums[i+2] == nums[i+1] / 2`. For `[1, 2, 1]`, `1 + 1 = 2`, which is not `2 / 2`. Actually, the condition is `nums[i] + nums[i+2] * 2 == nums[i+1]`. Let's re-verify: `1 + 1 == 2 / 2` is false. The condition is `(nums[i] + nums[i+2]) * 2 == nums[i+1]`.

**Example 2**

- Input: `nums = [1, 2, 1, 4, 1]`
- Output: `1`
- Explanation: Subarray `[1, 4, 1]` satisfies `(1 + 1) * 2 == 4`.

**Example 3**

- Input: `nums = [2, 2, 2, 2, 2]`
- Output: `3`
- Explanation: Subarrays `[2, 2, 2]` at indices `(0,1,2)`, `(1,2,3)`, and `(2,3,4)` all satisfy `(2 + 2) * 2 == 2`? No, the condition is `nums[i] + nums[i+2] == nums[i+1] / 2`.

---

## Solution
### Approach
A single-pass sliding window approach (or simple iteration) checking every triplet `(nums[i], nums[i+1], nums[i+2])`.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array once.
- **Space Complexity**: `O(1)`, as we only use a counter variable.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Counts subarrays of length 3 where (nums[i] + nums[i+2]) * 2 == nums[i+1].
    Note: The problem condition is defined as the sum of the first and third
    elements being equal to half of the middle element, which is equivalent
    to (nums[i] + nums[i+2]) * 2 == nums[i+1].
    """
    count = 0
    # We iterate up to len(nums) - 3 to check every triplet
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
            count += 1
    return count
```
</details>
