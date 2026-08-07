### 1. Description

You are given an integer array `nums`.

You **must** replace **exactly one** element in the array with **any** integer value in the range $[-10^{5}, 10^{5}]$ (inclusive).

After performing this single replacement, determine the **maximum possible product** of **any three** elements at **distinct indices** from the modified array.

Return an integer denoting the **maximum product** achievable.

### 2. Function Contract

**Inputs**

- `nums`: The integer array on which exactly one replacement must be performed.

The replaced index may be one of the three selected indices. All three factors in the final product must come from different indices of the modified array.

**Return value**

Return the greatest integer product obtainable after choosing both the replacement and the three selected indices optimally.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [-5,7,0]

**Output:** 3500000

**Explanation:**

Replacing 0 with -$10^{5}$ gives the array $[-5, 7, -10^{5}]$, which has a product $(-5) * 7 * (-10^{5}) = 3500000$. The maximum product is 3500000.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-4,-2,-1,-3]

**Output:** 1200000

**Explanation:**

Two ways to achieve the maximum product include:

- `[-4, -2, -3]` → replace -2 with $10^{5}$ → product = $(-4) * 10^{5} * (-3) = 1200000$.

- `[-4, -1, -3]` → replace -1 with $10^{5}$ → product = $(-4) * 10^{5} * (-3) = 1200000$.

The maximum product is 1200000.</div>
#### Example 3

<div class="example-block">
**Input:** nums = [0,10,0]

**Output:** 0

**Explanation:**

There is no way to replace an element with another integer and not have a 0 in the array. Hence, the product of all three elements will always be 0, and the maximum product is 0.

</div>

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$