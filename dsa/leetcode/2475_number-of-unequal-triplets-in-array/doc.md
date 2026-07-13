# Number of Unequal Triplets in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2475 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-unequal-triplets-in-array](https://leetcode.com/problems/number-of-unequal-triplets-in-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-unequal-triplets-in-array/).

### Goal
Given an array of integers, identify the total number of triplets (i, j, k) such that 0 <= i < j < k < n, and the values at these indices are mutually distinct (nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k]).

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 1000 and 1 <= nums[i] <= 1000.

**Return value**

- An integer representing the count of valid triplets that satisfy the inequality conditions.

### Examples
**Example 1**

- Input: `nums = [4,4,2,4,3]`
- Output: `3`
- Explanation: The valid triplets are (0, 2, 4), (1, 2, 4), and (2, 3, 4) corresponding to values (4, 2, 3).

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `0`
- Explanation: No three elements are distinct.

**Example 3**

- Input: `nums = [1,3,1,2,4]`
- Output: `7`

---

## Solution
### Approach
The problem can be solved using a frequency map (Hash Table) approach. By counting the occurrences of each number, we can calculate the number of triplets by considering the distribution of elements. If we pick a number with frequency `a`, another with frequency `b`, and a third with frequency `c`, the number of ways to form a triplet is `a * b * c`. Alternatively, a brute-force approach with O(n^3) is acceptable given the constraints (n <= 1000), but the frequency approach is O(n).

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the array once to build the frequency map and then iterate through the unique elements.
- **Space Complexity**: O(n) in the worst case to store the frequency map if all elements are unique.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums: list[int]) -> int:
    """
    Calculates the number of unequal triplets using a frequency map.
    If we have counts of each number, the number of triplets (i, j, k)
    with distinct values is the sum of products of frequencies of any
    three distinct numbers.
    """
    counts = list(Counter(nums).values())
    n = len(counts)
    triplets = 0

    # Iterate through all combinations of three distinct values
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triplets += counts[i] * counts[j] * counts[k]

    return triplets
```
</details>
