# Separate the Digits in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2553 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [separate-the-digits-in-an-array](https://leetcode.com/problems/separate-the-digits-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/separate-the-digits-in-an-array/).

### Goal
Given an array of positive integers, decompose each integer into its constituent decimal digits and return a new array containing all these digits in the order they appeared within the original sequence.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) representing the flattened sequence of all digits extracted from the input numbers.

### Examples
**Example 1**

- Input: `nums = [13, 25, 83, 77]`
- Output: `[1, 3, 2, 5, 8, 3, 7, 7]`

**Example 2**

- Input: `nums = [7, 1, 3, 9]`
- Output: `[7, 1, 3, 9]`

**Example 3**

- Input: `nums = [10, 20, 30]`
- Output: `[1, 0, 2, 0, 3, 0]`

---

## Solution
### Approach
The problem is a straightforward simulation. It involves iterating through each integer in the input array, converting the integer into its individual digits (either via string conversion or mathematical modulo/division operations), and appending these digits to a result list.

### Complexity Analysis
- **Time Complexity**: `O(N * K)`, where `N` is the number of elements in the input array and `K` is the average number of digits per integer. Since `K` is bounded by the maximum value of the integers (log10(max_val)), this is effectively linear relative to the total number of digits.
- **Space Complexity**: `O(N * K)` to store the resulting list of digits.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Decomposes each integer in the input list into its individual digits
    and returns them as a flat list.
    """
    result = []
    for num in nums:
        # Convert number to string to iterate over digits
        for digit in str(num):
            result.append(int(digit))
    return result
```
</details>
