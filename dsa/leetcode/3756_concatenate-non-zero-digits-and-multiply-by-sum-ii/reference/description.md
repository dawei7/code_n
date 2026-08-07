## Description

You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where $\text{queries}[i] = [l_{i}, r_{i}]$.

For each $\text{queries}[i]$, extract the **substring** $s[l_{i}..r_{i}]$. Then, perform the following:

- Form a new integer `x` by concatenating all the **non-zero digits** from the substring in their original order. If there are no non-zero digits, $x = 0$.

- Let `sum` be the **sum of digits** in `x`. The answer is $x * sum$.

Return an array of integers `answer` where $\text{answer}[i]$ is the answer to the $$i^{\text{th}}$$ query.

Since the answers may be very large, return them **modulo** $10^{9} + 7$.
### Function Contract

**Inputs**

- `s`: A nonempty string whose characters are decimal digits.
- `queries`: An array of inclusive index pairs `[l_i, r_i]` into `s`.

Let $m = \lvert\texttt{s}\rvert$ and $q = \lvert\texttt{queries}\rvert$. Each query is evaluated independently against the original string; removing zeros does not modify `s` or shift later query indices.

**Return value**

Return an array of $q$ integers. For each query, concatenate its nonzero digits in order, multiply that value by their digit sum, and return the product modulo $10^9+7$.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "10203004", queries = [[0,7],[1,3],[4,6]]

**Output:** [12340, 4, 9]

**Explanation:**

- $s[0..7] = "10203004"$

		<li>$x = 1234$

- $sum = 1 + 2 + 3 + 4 = 10$

- Therefore, answer is $1234 * 10 = 12340$.

	</li>
- $s[1..3] = "020"$

		<li>$x = 2$

- $sum = 2$

- Therefore, the answer is $2 * 2 = 4$.

	</li>
- $s[4..6] = "300"$

		<li>$x = 3$

- $sum = 3$

- Therefore, the answer is $3 * 3 = 9$.

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** s = "1000", queries = [[0,3],[1,1]]

**Output:** [1, 0]

**Explanation:**

- $s[0..3] = "1000"$

		<li>$x = 1$

- $sum = 1$

- Therefore, the answer is $1 * 1 = 1$.

	</li>
- $s[1..1] = "0"$

		<li>$x = 0$

- $sum = 0$

- Therefore, the answer is $0 * 0 = 0$.

	</li>

</div>
#### Example 3

<div class="example-block">
**Input:** s = "9876543210", queries = [[0,9]]

**Output:** [444444137]

**Explanation:**

- $s[0..9] = "9876543210"$

		<li>$x = 987654321$

- $sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45$

- Therefore, the answer is $987654321 * 45 = 44444444445$.

- We return $44444444445 modulo (10^{9} + 7) = 444444137$.

	</li>

</div>
### Constraints

- $1 \le m = \text{s.length} \le 10^{5}$

- `s` consists of digits only.

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i] = [l_{i}, r_{i}]$

- $0 \le l_{i} \le r_{i} < m$