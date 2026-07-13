# Max Pair Sum in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2815 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [max-pair-sum-in-an-array](https://leetcode.com/problems/max-pair-sum-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/max-pair-sum-in-an-array/).

### Goal
Given an array of integers, identify pairs of numbers that share the same maximum digit. Among all such valid pairs, calculate their sums and return the largest sum found. If no such pair exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the maximum sum of a pair of numbers that share the same maximum digit, or -1 if no such pair can be formed.

### Examples
**Example 1**

- Input: `nums = [51, 71, 17, 24, 42]`
- Output: `88`
- Explanation: The pairs (51, 71) share max digit 7 (sum 122 is not possible as 51 has max digit 5). The pairs (17, 71) share max digit 7, sum 88. (24, 42) share max digit 4, sum 66. Max is 88.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `-1`
- Explanation: No two numbers share the same maximum digit.

**Example 3**

- Input: `nums = [31, 25, 7, 59, 73]`
- Output: `104`
- Explanation: 7 and 73 share max digit 7, sum 80. 25 and 59 share max digit 5, sum 84. 31 and 73 share max digit 7, sum 104. Max is 104.

---

## Solution
### Approach
The solution utilizes a Hash Map (dictionary) to group numbers by their maximum digit. By iterating through the array once, we maintain the largest value encountered so far for each digit (0-9). When a new number is processed, we check if its maximum digit has been seen before; if so, we calculate the potential sum and update the global maximum.

### Complexity Analysis
- **Time Complexity**: `O(n * d)`, where `n` is the number of elements in the array and `d` is the number of digits in the largest integer (to find the max digit). Since `d` is small (max 10 for 32-bit integers), this is effectively `O(n)`.
- **Space Complexity**: `O(1)`, as the hash map stores at most 10 entries (one for each possible digit 0-9).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    def get_max_digit(n: int) -> int:
        max_d = 0
        while n > 0:
            max_d = max(max_d, n % 10)
            n //= 10
        return max_d

    # Stores the largest number found so far for each max digit (0-9)
    max_val_for_digit = {}
    max_sum = -1

    for num in nums:
        d = get_max_digit(num)

        if d in max_val_for_digit:
            # If we have seen this max digit before, calculate the sum
            current_sum = num + max_val_for_digit[d]
            max_sum = max(max_sum, current_sum)
            # Update the stored value if the current number is larger
            max_val_for_digit[d] = max(max_val_for_digit[d], num)
        else:
            # First time seeing this max digit
            max_val_for_digit[d] = num

    return max_sum
```
</details>
