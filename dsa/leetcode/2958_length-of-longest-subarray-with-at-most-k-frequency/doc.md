# Length of Longest Subarray With at Most K Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2958 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [length-of-longest-subarray-with-at-most-k-frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/).

### Goal
Given an integer array and an integer `k`, determine the length of the longest contiguous subarray where no element appears more than `k` times.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum allowed frequency of any element within the subarray.

**Return value**

- An integer representing the maximum length of a valid subarray.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1, 2, 3, 1, 2], k = 2`
- Output: `6`

**Example 2**

- Input: `nums = [1, 2, 1, 2, 1, 2, 1], k = 1`
- Output: `2`

**Example 3**

- Input: `nums = [5, 5, 5, 5, 5, 5, 5], k = 4`
- Output: `4`

---

## Solution
### Approach
The problem is solved using the **Sliding Window** technique combined with a **Hash Map** (or frequency array) to track the counts of elements within the current window. By expanding the right boundary and shrinking the left boundary whenever a frequency exceeds `k`, we maintain a valid window state efficiently.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. Each element is visited at most twice (once by the right pointer and once by the left pointer).
- **Space Complexity**: `O(m)`, where `m` is the number of unique elements in the array, as the hash map stores the frequency of each distinct integer.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest subarray where no element appears more than k times.
    Uses a sliding window approach with a hash map to track frequencies.
    """
    max_length = 0
    left = 0
    counts = defaultdict(int)

    for right in range(len(nums)):
        # Add the current element to the window
        counts[nums[right]] += 1

        # If the frequency exceeds k, shrink the window from the left
        while counts[nums[right]] > k:
            counts[nums[left]] -= 1
            left += 1

        # Update the maximum length found so far
        max_length = max(max_length, right - left + 1)

    return max_length
```
</details>
