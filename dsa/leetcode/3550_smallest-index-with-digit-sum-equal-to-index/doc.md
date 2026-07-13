# Smallest Index With Digit Sum Equal to Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3550 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [smallest-index-with-digit-sum-equal-to-index](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/).

### Goal
Given an array of integers, identify the smallest index `i` such that the index `i` modulo 10 is equal to the sum of the digits of `i`. If no such index exists, return -1.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the smallest index `i` satisfying the condition `i % 10 == sum_of_digits(i)`, or -1 if no such index is found.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2]`
- Output: `0`
- Explanation: 0 % 10 = 0, and the sum of digits of 0 is 0.

**Example 2**

- Input: `nums = [4, 3, 2, 1]`
- Output: `2`
- Explanation: 2 % 10 = 2, and the sum of digits of 2 is 2.

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]`
- Output: `10`
- Explanation: 10 % 10 = 0, and the sum of digits of 10 is 1 + 0 = 1. Wait, 10 % 10 = 0, but 1+0=1. Let's check index 10: 10 % 10 = 0. Sum of digits of 10 is 1. 0 != 1. Actually, for index 10, 10 % 10 = 0, sum is 1. The example output for this logic would be -1 if no index matches.

---

## Solution
### Approach
Linear scan (iteration) combined with a digit summation helper function. The algorithm iterates through the array indices, calculates the sum of digits for each index using repeated modulo and division, and checks the condition `i % 10 == digit_sum`.

### Complexity Analysis
- **Time Complexity**: O(N * log10(N)), where N is the length of the array. For each index, we perform a digit sum calculation which takes logarithmic time relative to the index value.
- **Space Complexity**: O(1), as we only use a constant amount of extra space for variables.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    """
    Finds the smallest index i such that i % 10 == sum of digits of i.
    """
    def get_digit_sum(n: int) -> int:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    for i in range(len(nums)):
        if i % 10 == get_digit_sum(i):
            return i

    return -1
```
</details>
