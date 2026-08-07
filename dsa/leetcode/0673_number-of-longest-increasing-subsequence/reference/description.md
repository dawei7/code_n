## Description

Given an integer array `nums`, return *the number of longest increasing subsequences.*

**Notice** that the sequence has to be **strictly** increasing.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [1,3,5,4,7]`
- **Output:** `2`
- **Explanation:** The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
#### Example 2

- **Input:** `nums = [2,2,2,2,2]`
- **Output:** `5`
- **Explanation:** The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
### Constraints

- $1 \le \text{nums.length} \le 2000$

- $-10^{6} \le \text{nums}[i] \le 10^{6}$

- The answer is guaranteed to fit inside a 32-bit integer.