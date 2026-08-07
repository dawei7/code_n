### 1. Description

You are given an integer array `nums` of length `n` and an integer `k`.

Pick a **subsequence** with indices $0 \le i_{1} < i_{2} < ... < i_{m} < n$ such that:

- For every $1 \le t < m$, $i_{t}+1 - i_{t} \ge k$.

- The selected values form a **strictly alternating** sequence. In other words, either:

		<li>$nums[i_{1}] < nums[i_{2}] > nums[i_{3}] < ...$, or

- $nums[i_{1}] > nums[i_{2}] < nums[i_{3}] > ...$

	</li>

A **subsequence** of length 1 is also considered **strictly** alternating. The score of a **valid** subsequence is the **sum** of its selected values.

Return an integer denoting the **maximum** possible **score** of a valid subsequence.

### 2. Function Contract

**Inputs**

- `nums`: The non-empty positive-integer array from which indices are selected.
- `k`: The minimum difference between each pair of consecutive selected indices.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return the maximum sum of a non-empty subsequence whose consecutive selected indices differ by at least `k` and whose consecutive value comparisons are strict and alternate direction. A singleton is always valid.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [5,4,2], k = 2

**Output:** 7

**Explanation:**

An optimal choice is indices `[0, 2]`, which gives values `[5, 2]`.

- The distance condition holds because $2 - 0 = 2 \ge k$.

- The values are strictly alternating because `5 > 2`.

The score is $5 + 2 = 7$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,5,4,2,4], k = 1

**Output:** 14

**Explanation:**

An optimal choice is indices `[0, 1, 3, 4]`, which gives values `[3, 5, 2, 4]`.

- The distance condition holds because each pair of consecutive chosen indices differs by at least $k = 1$.

- The values are strictly alternating since `3 < 5 > 2 < 4`.

The score is $3 + 5 + 2 + 4 = 14$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5], k = 1

**Output:** 5

**Explanation:**

The only valid subsequence is `[5]`. A subsequence with 1 element is always strictly alternating, so the score is 5.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le k \le n$