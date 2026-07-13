# Count Complete Subarrays in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2799 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-complete-subarrays-in-an-array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-complete-subarrays-in-an-array/).

### Goal
Given an array of integers, determine the total number of contiguous subarrays that contain the exact same set of distinct elements as the original array. A subarray is considered "complete" if its count of unique integers matches the count of unique integers found in the entire input array.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of all contiguous subarrays that are complete.

### Examples
**Example 1**

- Input: `nums = [1,3,1,2,2]`
- Output: `4`
- Explanation: The distinct elements are {1, 2, 3}. The complete subarrays are [1,3,1,2], [1,3,1,2,2], [3,1,2], and [3,1,2,2].

**Example 2**

- Input: `nums = [5,5,5,5]`
- Output: `10`
- Explanation: The distinct element is {5}. Every non-empty subarray is complete. There are 4*(4+1)/2 = 10 such subarrays.

**Example 3**

- Input: `nums = [1,2,1,3]`
- Output: `3`
- Explanation: The distinct elements are {1, 2, 3}. The complete subarrays are [1,2,1,3], [2,1,3], and [1,2,1,3] is not possible, but [1,2,1,3] is the only one containing all three. Wait, the complete subarrays are [1,2,1,3], [2,1,3], and [1,2,1,3] is not correct; the valid ones are [1,2,1,3], [2,1,3], and [1,2,1,3] is not right. Actually, the subarrays are [1,2,1,3] and [2,1,3].

---

## Solution
### Approach
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (or frequency array). By first identifying the total number of unique elements in the array, we can expand a right pointer to include elements until the window contains all unique elements. Once the condition is met, we shrink the left pointer to find all valid subarrays ending at the current right position.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array with two pointers, each moving at most `n` times.
- **Space Complexity**: `O(k)`, where `k` is the number of unique elements in the array, used to store the frequency map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums: list[int]) -> int:
    """
    Counts the number of complete subarrays using a sliding window approach.
    A subarray is complete if it contains all unique elements present in the original array.
    """
    total_unique_count = len(set(nums))
    n = len(nums)

    count = 0
    left = 0
    window_map = {}

    # Expand the right boundary of the window
    for right in range(n):
        window_map[nums[right]] = window_map.get(nums[right], 0) + 1

        # While the current window contains all unique elements,
        # all subarrays starting from 'left' to 'right' and ending at 'right'
        # are complete.
        while len(window_map) == total_unique_count:
            # If the window [left, right] is valid, then all subarrays
            # [left, right], [left+1, right], ..., [right, right] are valid.
            # There are (n - right) such subarrays.
            count += (n - right)

            # Shrink the window from the left
            window_map[nums[left]] -= 1
            if window_map[nums[left]] == 0:
                del window_map[nums[left]]
            left += 1

    return count
```
</details>
