## Description

Given an integer array `nums`, return the **length** of the **longest subarray** that has a bitwise XOR of zero and contains an **equal** number of **even** and **odd** numbers. If no such subarray exists, return 0.
### Function Contract

**Inputs**

- `nums`: The integer array from which a contiguous, nonempty range may be selected.

The parity count treats zero as even. Both the zero-XOR and equal-parity-count requirements must hold for the same selected indices.

**Return value**

Return the maximum valid subarray length, or `0` when no nonempty subarray satisfies both requirements.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [3,1,3,2,0]

**Output:** 4

**Explanation:**

The subarray `[1, 3, 2, 0]` has bitwise XOR $1 XOR 3 XOR 2 XOR 0 = 0$ and contains 2 even and 2 odd numbers.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,2,8,5,4,14,9,15]

**Output:** 8

**Explanation:**

The whole array has bitwise XOR `0` and contains 4 even and 4 odd numbers.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [0]

**Output:** 0

**Explanation:**

No non-empty subarray satisfies both conditions.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{9}$