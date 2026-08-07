### 1. Description

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

- Increase or decrease any element of `nums` by 1.

Return the **minimum** number of operations required to ensure that **at least** one subarray of size `k` in `nums` has all elements equal.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,-3,2,1,-4,6], k = 3

**Output:** 5

**Explanation:**

- Use 4 operations to add 4 to $\text{nums}[1]$. The resulting array is `[4, 1, 2, 1, -4, 6]`.

- Use 1 operation to subtract 1 from $\text{nums}[2]$. The resulting array is `[4, 1, 1, 1, -4, 6]`.

- The array now contains a subarray `[1, 1, 1]` of size $k = 3$ with all elements equal. Hence, the answer is 5.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-2,-2,3,1,4], k = 2

**Output:** 0

**Explanation:**

- The subarray `[-2, -2]` of size $k = 2$ already contains all equal elements, so no operations are needed. Hence, the answer is 0.

</div>

### 4. Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $-10^{6} \le \text{nums}[i] \le 10^{6}$

- $2 \le k \le \text{nums.length}$