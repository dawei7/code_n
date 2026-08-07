## Description

Given an integer array `nums`, return `0`* if the sum of the digits of the minimum integer in *`nums`* is odd, or *`1`* otherwise*.
### Function Contract

**Input**

- `nums`: a non-empty integer array.

Let $n$ be the length of `nums`, and let $D$ be the number of decimal digits in `min(nums)`.

**Return value**

- `0` if the sum of the decimal digits of `min(nums)` is odd.
- `1` if that digit sum is even.

Repeated occurrences of the minimum do not change the answer because the contract uses the minimum value, not its frequency.

### Examples
#### Example 1

- **Input:** `nums = [34,23,1,24,75,33,54,8]`
- **Output:** `0`
- **Explanation:** The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
#### Example 2

- **Input:** `nums = [99,77,33,66,55]`
- **Output:** `1`
- **Explanation:** The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$