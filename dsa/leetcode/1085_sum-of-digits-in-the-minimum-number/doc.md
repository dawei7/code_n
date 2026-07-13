# Sum of Digits in the Minimum Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1085 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-digits-in-the-minimum-number](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/).

### Goal
Find the smallest number in the array, compute the sum of its decimal digits, and return `1` if that sum is even or `0` if that sum is odd.

### Function Contract
**Inputs**

- `nums`: List of positive integers.

**Return value**

`1` when the minimum number's digit sum is even; otherwise `0`.

### Examples
**Example 1**

- Input: `nums = [34, 23, 1, 24, 75, 33, 54, 8]`
- Output: `0`

**Example 2**

- Input: `nums = [99, 77, 33, 66, 55]`
- Output: `1`

**Example 3**

- Input: `nums = [10, 20, 30]`
- Output: `0`

---

## Solution
### Approach
Scan the array to find the minimum value. Then repeatedly take `value % 10` and divide by `10` to sum its digits. The final parity of the digit sum determines the return value.

### Complexity Analysis
- **Time Complexity**: `O(n + d)`, where `n` is the array length and `d` is the number of digits in the minimum value.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
