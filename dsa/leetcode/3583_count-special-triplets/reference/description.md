### 1. Description

You are given an integer array `nums`.

A **special triplet** is defined as a triplet of indices `(i, j, k)` such that:

- $0 \le i < j < k < n$, where $n = \text{nums.length}$

- $\text{nums}[i] = \text{nums}[j] * 2$

- $\text{nums}[k] = \text{nums}[j] * 2$

Return the total number of **special triplets** in the array.

Since the answer may be large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [6,3,6]

**Output:** 1

**Explanation:**

The only special triplet is $(i, j, k) = (0, 1, 2)$, where:

- $\text{nums}[0] = 6$, $\text{nums}[1] = 3$, $\text{nums}[2] = 6$

- $\text{nums}[0] = \text{nums}[1] * 2 = 3 * 2 = 6$

- $\text{nums}[2] = \text{nums}[1] * 2 = 3 * 2 = 6$

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,1,0,0]

**Output:** 1

**Explanation:**

The only special triplet is $(i, j, k) = (0, 2, 3)$, where:

- $\text{nums}[0] = 0$, $\text{nums}[2] = 0$, $\text{nums}[3] = 0$

- $\text{nums}[0] = \text{nums}[2] * 2 = 0 * 2 = 0$

- $\text{nums}[3] = \text{nums}[2] * 2 = 0 * 2 = 0$

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [8,4,2,8,4]

**Output:** 2

**Explanation:**

There are exactly two special triplets:

- $(i, j, k) = (0, 1, 3)$

		<li>$\text{nums}[0] = 8$, $\text{nums}[1] = 4$, $\text{nums}[3] = 8$

- $\text{nums}[0] = \text{nums}[1] * 2 = 4 * 2 = 8$

- $\text{nums}[3] = \text{nums}[1] * 2 = 4 * 2 = 8$

	</li>
- $(i, j, k) = (1, 2, 4)$

		<li>$\text{nums}[1] = 4$, $\text{nums}[2] = 2$, $\text{nums}[4] = 4$

- $\text{nums}[1] = \text{nums}[2] * 2 = 2 * 2 = 4$

- $\text{nums}[4] = \text{nums}[2] * 2 = 2 * 2 = 4$

	</li>

</div>

### 4. Constraints

- $3 \le n = \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$