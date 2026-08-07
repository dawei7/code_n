## Description

You are given an integer array `nums` of length `n` where each element is a non-negative integer.

Select **two** subsequences of `nums` (they may be empty and are **allowed** to **overlap**), each preserving the original order of elements, and let:

- `X` be the bitwise XOR of all elements in the first subsequence.

- `Y` be the bitwise XOR of all elements in the second subsequence.

Return the **maximum** possible value of `X XOR Y`.

**Note:** The XOR of an **empty** subsequence is 0.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 3

**Explanation:**

Choose subsequences:

- First subsequence `[2]`, whose XOR is 2.

- Second subsequence `[2,3]`, whose XOR is 1.

Then, XOR of both subsequences = $2 XOR 1 = 3$.

This is the maximum XOR value achievable from any two subsequences.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,2]

**Output:** 7

**Explanation:**

Choose subsequences:

- First subsequence `[5]`, whose XOR is 5.

- Second subsequence `[2]`, whose XOR is 2.

Then, XOR of both subsequences = $5 XOR 2 = 7$.

This is the maximum XOR value achievable from any two subsequences.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$