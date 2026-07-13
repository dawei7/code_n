# Count Partitions with Even Sum Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3432 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-partitions-with-even-sum-difference](https://leetcode.com/problems/count-partitions-with-even-sum-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-partitions-with-even-sum-difference/).

### Goal
Given an array of integers, determine how many ways the array can be split into two non-empty contiguous subarrays (a left part and a right part) such that the difference between the sum of the left part and the sum of the right part is an even number.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- An integer representing the count of valid partitions where `(sum(left) - sum(right))` is even.

### Examples
**Example 1**

- Input: `nums = [10, 10, 3, 7, 6]`
- Output: `4`
- Explanation: The partitions are:
  - [10] and [10, 3, 7, 6] (sum 10, sum 26, diff -16, even)
  - [10, 10] and [3, 7, 6] (sum 20, sum 16, diff 4, even)
  - [10, 10, 3] and [7, 6] (sum 23, sum 13, diff 10, even)
  - [10, 10, 3, 7] and [6] (sum 30, sum 6, diff 24, even)

**Example 2**

- Input: `nums = [1, 2, 2]`
- Output: `0`

**Example 3**

- Input: `nums = [2, 4, 6]`
- Output: `2`

---

## Solution
### Approach
The problem can be solved using a Prefix Sum approach. By calculating the total sum of the array first, we can determine the sum of the right partition in constant time as we iterate through the array: `right_sum = total_sum - left_sum`. The condition `(left_sum - right_sum) % 2 == 0` is mathematically equivalent to checking if `(left_sum - (total_sum - left_sum))` is even, which simplifies to `(2 * left_sum - total_sum)` being even. Since `2 * left_sum` is always even, the condition is satisfied if and only if `total_sum` is even.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we perform a single pass to calculate the total sum and another pass to evaluate the partitions.
- **Space Complexity**: `O(1)`, as we only store a few integer variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the number of partitions where the difference between
    the left sum and right sum is even.
    """
    total_sum = sum(nums)
    left_sum = 0
    count = 0

    # We iterate up to len(nums) - 1 because the right partition
    # must be non-empty.
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum = total_sum - left_sum

        if (left_sum - right_sum) % 2 == 0:
            count += 1

    return count
```
</details>
