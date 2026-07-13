# Minimum Element After Replacement With Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3300 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-element-after-replacement-with-digit-sum](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/).

### Goal
Given an array of integers, transform each element by replacing it with the sum of its individual digits. After performing this transformation on every element in the array, return the smallest value present in the resulting collection.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the minimum value found after replacing each element with its digit sum.

### Examples
**Example 1**

- Input: `nums = [10, 12, 13, 14]`
- Output: `1`
- Explanation: Digit sums are [1, 3, 4, 5]. The minimum is 1.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `1`
- Explanation: Digit sums are [1, 2, 3, 4]. The minimum is 1.

**Example 3**

- Input: `nums = [999, 19, 199]`
- Output: `10`
- Explanation: Digit sums are [27, 10, 19]. The minimum is 10.

---

## Solution
### Approach
The solution utilizes a simple iterative transformation approach. For each integer, we compute the sum of its digits using the modulo operator (`% 10`) to extract the last digit and integer division (`// 10`) to shift the number until it reaches zero. We then track the minimum value encountered during this process.

### Complexity Analysis
- **Time Complexity**: `O(n * d)`, where `n` is the number of elements in the array and `d` is the average number of digits in the integers. Since the numbers are typically bounded (e.g., 32-bit integers), `d` is effectively constant, making the complexity `O(n)`.
- **Space Complexity**: `O(1)`, as we only store the running minimum and temporary variables for digit summation, requiring no additional data structures proportional to the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def get_digit_sum(n: int) -> int:
    """Helper function to calculate the sum of digits of an integer."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def solve(nums: List[int]) -> int:
    """
    Transforms each element in nums to its digit sum and returns the minimum.
    """
    min_val = float('inf')

    for num in nums:
        digit_sum = get_digit_sum(num)
        if digit_sum < min_val:
            min_val = digit_sum

    return int(min_val)
```
</details>
