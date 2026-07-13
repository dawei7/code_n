# Minimum Number of Operations to Make All Array Elements Equal to 1

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2654 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-operations-to-make-all-array-elements-equal-to-1](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/).

### Goal
Given an array of integers, determine the minimum number of operations required to transform every element in the array to 1. In one operation, you can select any two adjacent elements and replace one of them with their greatest common divisor (GCD).

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the minimum operations needed, or -1 if it is impossible to make all elements 1.

### Examples
**Example 1**

- Input: `nums = [2, 6, 3, 4]`
- Output: `4`

**Example 2**

- Input: `nums = [2, 10, 6, 14]`
- Output: `-1`

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `0`

---

## Solution
### Approach
The problem relies on the property that if the GCD of the entire array is greater than 1, it is impossible to create a 1, returning -1. If there is already a 1 in the array, the answer is `(n - count_of_ones)`. If no 1 exists, we must find the shortest subarray whose GCD is 1. The length of this subarray `L` allows us to create a 1 in `L-1` operations, and then we use that 1 to convert the remaining `n-1` elements, resulting in `(L-1) + (n-1)` operations.

### Complexity Analysis
- **Time Complexity**: `O(n^2 + n * log(max(nums)))`, where `n` is the length of the array. We iterate through all possible subarrays to find the shortest one with a GCD of 1.
- **Space Complexity**: `O(1)`, as we only use a few variables for tracking the minimum length and GCD calculations.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math

def solve(nums: list[int]) -> int:
    n = len(nums)
    ones_count = nums.count(1)

    if ones_count > 0:
        return n - ones_count

    # Find the shortest subarray with GCD == 1
    min_len = float('inf')

    for i in range(n):
        current_gcd = nums[i]
        for j in range(i + 1, n):
            current_gcd = math.gcd(current_gcd, nums[j])
            if current_gcd == 1:
                min_len = min(min_len, j - i + 1)
                break

    if min_len == float('inf'):
        return -1

    # Operations = (min_len - 1) to create one '1'
    # + (n - 1) to propagate that '1' to the rest of the array
    return min_len - 1 + n - 1
```
</details>
