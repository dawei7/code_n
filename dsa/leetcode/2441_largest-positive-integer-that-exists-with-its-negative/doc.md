# Largest Positive Integer That Exists With Its Negative

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2441 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [largest-positive-integer-that-exists-with-its-negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/).

### Goal
Given an array of integers, identify the largest positive integer `k` such that `-k` is also present in the array. If no such pair exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the maximum value `k` where both `k` and `-k` are in the input list, or `-1` if no such pair is found.

### Examples
**Example 1**

- Input: `[-1, 2, -3, 3]`
- Output: `3`

**Example 2**

- Input: `[-1, 10, 6, 7, -7, 1]`
- Output: `7`

**Example 3**

- Input: `[-10, 8, 6, 7, -2, -3]`
- Output: `-1`

---

## Solution
### Approach
The optimal approach utilizes a Hash Set for O(1) average-time complexity lookups. By iterating through the array and storing elements in a set, we can check for the existence of the negation of each positive integer encountered. Alternatively, a two-pointer approach on a sorted array can achieve the same result.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the array, as we perform a single pass to populate the set and a second pass (or concurrent check) to find the maximum.
- **Space Complexity**: `O(n)` to store the elements in a hash set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the largest positive integer k such that -k exists in the list.
    Uses a set for O(1) lookups.
    """
    num_set = set(nums)
    max_k = -1

    for x in nums:
        if x > 0 and -x in num_set:
            if x > max_k:
                max_k = x

    return max_k
```
</details>
