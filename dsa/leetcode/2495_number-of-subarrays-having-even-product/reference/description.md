### 1. Description

Given a **0-indexed** integer array `nums`, return *the number of subarrays of *`nums`* having an even product*.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** `nums = [9,6,7,13]`
- **Output:** `6`
- **Explanation:** There are 6 subarrays with an even product:
- nums[0..1] = 9 * 6 = 54.
- nums[0..2] = 9 * 6 * 7 = 378.
- nums[0..3] = 9 * 6 * 7 * 13 = 4914.
- nums[1..1] = 6.
- nums[1..2] = 6 * 7 = 42.
- nums[1..3] = 6 * 7 * 13 = 546.

#### Example 2

- **Input:** `nums = [7,3,5]`
- **Output:** `0`
- **Explanation:** There are no subarrays with an even product.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$
