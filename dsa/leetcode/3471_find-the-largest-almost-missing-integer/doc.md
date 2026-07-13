# Find the Largest Almost Missing Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3471 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-largest-almost-missing-integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-largest-almost-missing-integer/).

### Goal
Given an integer array `nums` and an integer `k`, identify the largest integer that appears in exactly one subarray of length `k`. If no such integer exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the length of the subarrays to consider.

**Return value**

- An integer representing the largest value that appears in exactly one subarray of length `k`, or -1 if no such value exists.

### Examples
**Example 1**

- Input: `nums = [3, 9, 2, 1, 7], k = 3`
- Output: `7`

**Example 2**

- Input: `nums = [3, 9, 7, 2, 1, 7], k = 2`
- Output: `3`

**Example 3**

- Input: `nums = [0, 0], k = 1`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using a frequency counting approach. We iterate through all possible subarrays of length `k` using a sliding window or simple slicing. For each subarray, we count the occurrences of its elements. We then track how many distinct subarrays each unique integer appears in. Finally, we filter for integers that appear in exactly one subarray and return the maximum among them.

### Complexity Analysis
- **Time Complexity**: O(n * k), where n is the length of the array. We iterate through n-k+1 subarrays, and for each, we process k elements.
- **Space Complexity**: O(n), as we store the frequency of each integer across the subarrays in a hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    # Map to store how many subarrays of length k contain a specific number
    count_map = defaultdict(int)
    n = len(nums)

    # Iterate through all possible subarrays of length k
    for i in range(n - k + 1):
        subarray = nums[i : i + k]
        # Use a set to ensure we only count the number once per subarray
        unique_elements = set(subarray)
        for val in unique_elements:
            count_map[val] += 1

    # Find the largest number that appeared in exactly one subarray
    max_val = -1
    for val, count in count_map.items():
        if count == 1:
            if val > max_val:
                max_val = val

    return max_val
```
</details>
