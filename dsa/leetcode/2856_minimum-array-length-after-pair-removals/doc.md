# Minimum Array Length After Pair Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2856 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-array-length-after-pair-removals](https://leetcode.com/problems/minimum-array-length-after-pair-removals/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-array-length-after-pair-removals/).

### Goal
Given a sorted array of integers, you are allowed to repeatedly select two distinct elements from the array and remove them. The objective is to minimize the final length of the array after performing as many such removals as possible.

### Function Contract
**Inputs**

- `nums`: A non-decreasingly sorted list of integers.

**Return value**

- An integer representing the minimum possible length of the array after performing the optimal sequence of removals.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`

**Example 2**

- Input: `nums = [1, 1, 2, 2, 3, 3]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 1, 2, 2]`
- Output: `2`

---

## Solution
### Approach
The problem can be solved using a Greedy approach combined with the Pigeonhole Principle. Since the array is sorted, the most frequent element determines the bottleneck. If the count of the most frequent element exceeds half the array length, those excess elements cannot be paired with others, leaving them as the remainder. Otherwise, if the total length is even, we can reduce the array to 0; if odd, we can reduce it to 1.

### Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the length of the array, as we iterate through the array to count frequencies or use a two-pointer approach.
- **Space Complexity**: `O(1)` if using the two-pointer approach on the sorted array, or `O(N)` if using a hash map for frequency counting.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums: list[int]) -> int:
    """
    The optimal strategy is to identify the most frequent element.
    Let 'max_freq' be the frequency of the most common element and 'n' be the total length.
    If max_freq > n / 2, the minimum remaining length is (max_freq - (n - max_freq)) = 2 * max_freq - n.
    Otherwise, the minimum length is n % 2.
    """
    n = len(nums)
    if n == 0:
        return 0

    counts = Counter(nums)
    max_freq = max(counts.values())

    if max_freq > n // 2:
        return 2 * max_freq - n
    else:
        return n % 2
```
</details>
