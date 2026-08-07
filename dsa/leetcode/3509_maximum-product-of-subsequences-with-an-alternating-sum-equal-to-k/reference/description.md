## Description

You are given an integer array `nums` and two integers, `k` and `limit`. Your task is to find a non-empty **subsequence** of `nums` that:

- Has an **alternating sum** equal to `k`.

- **Maximizes** the product of all its numbers *without the product exceeding* `limit`.

Return the *product* of the numbers in such a subsequence. If no subsequence satisfies the requirements, return -1.

The **alternating sum** of a **0-indexed** array is defined as the **sum** of the elements at **even** indices **minus** the **sum** of the elements at **odd** indices.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3], k = 2, limit = 10

**Output:** 6

**Explanation:**

The subsequences with an alternating sum of 2 are:

- `[1, 2, 3]`

		<li>Alternating Sum: $1 - 2 + 3 = 2$

- Product: $1 * 2 * 3 = 6$

	</li>
- `[2]`

		<li>Alternating Sum: 2

- Product: 2

	</li>

The maximum product within the limit is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,2,3], k = -5, limit = 12

**Output:** -1

**Explanation:**

A subsequence with an alternating sum of exactly -5 does not exist.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,2,3,3], k = 0, limit = 9

**Output:** 9

**Explanation:**

The subsequences with an alternating sum of 0 are:

- `[2, 2]`

		<li>Alternating Sum: $2 - 2 = 0$

- Product: $2 * 2 = 4$

	</li>
- `[3, 3]`

		<li>Alternating Sum: $3 - 3 = 0$

- Product: $3 * 3 = 9$

	</li>
- `[2, 2, 3, 3]`

		<li>Alternating Sum: $2 - 2 + 3 - 3 = 0$

- Product: $2 * 2 * 3 * 3 = 36$

	</li>

The subsequence `[2, 2, 3, 3]` has the greatest product with an alternating sum equal to `k`, but `36 > 9`. The next greatest product is 9, which is within the limit.

</div>
### Constraints

- $1 \le \text{nums.length} \le 150$

- $0 \le \text{nums}[i] \le 12$

- $-10^{5} \le k \le 10^{5}$

- $1 \le limit \le 5000$