### 1. Description

You are given an integer array `nums` and a positive integer `k`.

You must choose **exactly** one subarray of `nums` and perform **exactly** one of the following operations:

- Multiply each number in the chosen subarray by `k`.

- Divide each number in the chosen subarray by `k`.

		- When dividing a positive number by `k`, use the **floor** value of the division result.

- When dividing a negative number by `k`, use the **ceiling** value of the division result.

Return the **maximum** possible sum of a **non-empty** subarray in the resulting array.

Note that the subarray chosen for the operation and the subarray chosen for the sum may be **different**.

### 2. Function Contract

`solve(nums, k) -> int`

**Inputs**

- `nums`: A nonempty integer array from which both the operation subarray and the final sum subarray are selected.
- `k`: A positive integer used as either the common multiplier or the common divisor for exactly one nonempty operation subarray.

**Output**

Return the maximum sum of a nonempty contiguous subarray after performing exactly one permitted operation. When division is chosen, each transformed value is independently truncated toward zero. The operation range and the range whose sum is returned may be different.

### 3. Examples

#### Example 1

- **Input:** nums = [1,-2,3,4,-5], k = 2

- **Output:** 14

- **Explanation:** 

- Multiply each number in the subarray `[3, 4]` by 2.

- This results in `nums = [1, -2, 6, 8, -5]`.

- The subarray with the largest sum is `[6, 8]`, so the output is $6 + 8 = 14$.

#### Example 2

- **Input:** nums = [-5,-4,-3], k = 2

- **Output:** -1

- **Explanation:** 

- Divide each number in the subarray `[-3]` by 2.

- This results in `nums = [-5, -4, -1]`.

- The subarray with the largest sum is `[-1]`, so the output is -1.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le 10^{5}$
