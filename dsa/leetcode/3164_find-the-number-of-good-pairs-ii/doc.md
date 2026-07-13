# Find the Number of Good Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3164 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-good-pairs-ii](https://leetcode.com/problems/find-the-number-of-good-pairs-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-good-pairs-ii/).

### Goal
Given two integer arrays `nums1` and `nums2` and an integer `k`, identify the total count of "good pairs" (i, j). A pair (i, j) is considered good if `nums1[i]` is divisible by the product of `nums2[j]` and `k`. That is, `nums1[i] % (nums2[j] * k) == 0`.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.
- `k`: An integer multiplier.

**Return value**

- An integer representing the total count of indices (i, j) such that `nums1[i]` is divisible by `nums2[j] * k`.

### Examples
**Example 1**

- Input: `nums1 = [1, 3, 4], nums2 = [1, 3, 4], k = 1`
- Output: `5`

**Example 2**

- Input: `nums1 = [1, 2, 4, 12], nums2 = [2, 4], k = 3`
- Output: `2`

**Example 3**

- Input: `nums1 = [10, 20], nums2 = [1, 2], k = 2`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a Frequency Map (Hash Table) approach. By counting the occurrences of each number in `nums1`, we can iterate through each unique divisor `d = nums2[j] * k`. For each divisor, we iterate through its multiples up to the maximum value present in `nums1`, checking if those multiples exist in our frequency map. This avoids the O(N*M) brute force approach.

### Complexity Analysis
- **Time Complexity**: O(N + M + V log V), where N is the length of `nums1`, M is the length of `nums2`, and V is the maximum value in `nums1`. The harmonic series summation ensures the inner loop runs efficiently.
- **Space Complexity**: O(V), where V is the maximum value in `nums1`, used to store the frequency map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    # Count frequencies of numbers in nums1
    count1 = Counter(nums1)

    # Find the maximum value in nums1 to bound our search
    if not nums1:
        return 0
    max_val = max(nums1)

    total_good_pairs = 0

    # Count frequencies of divisors in nums2
    # We only care about unique values in nums2 to avoid redundant work
    count2 = Counter(nums2)

    # For each unique divisor d = nums2[j] * k
    for val, freq in count2.items():
        divisor = val * k

        # Iterate through multiples of the divisor: divisor, 2*divisor, 3*divisor...
        # up to max_val
        for multiple in range(divisor, max_val + 1, divisor):
            if multiple in count1:
                total_good_pairs += count1[multiple] * freq

    return total_good_pairs
```
</details>
