## Description

You are given two integers `l` and `r`.

An integer is called **good** if its digits form a **strictly monotone** sequence, meaning the digits are **strictly increasing** or **strictly decreasing**. All single-digit integers are considered good.

An integer is called **fancy** if it is good, or if the **sum of its digits** is good.

Return an integer representing the number of fancy integers in the range `[l, r]` (inclusive).

A sequence is said to be **strictly increasing** if each element is **strictly greater** than its previous one (if exists).

A sequence is said to be **strictly decreasing** if each element is **strictly less** than its previous one (if exists).
### Function Contract

**Inputs**

- `l`: The inclusive lower endpoint of the integer range.
- `r`: The inclusive upper endpoint, with $l \le r$.

Use each integer's ordinary decimal representation without leading zeros. For a number with digits $d_1,d_2,\ldots,d_k$, its digit sum is $d_1+d_2+\cdots+d_k$. A multi-digit sequence is strictly monotone only when every adjacent comparison points in the same strict direction; equal adjacent digits invalidate both directions.

**Return value**

Return an integer equal to the number of values $x$ satisfying $l\le x\le r$ for which $x$ is good, its digit sum is good, or both.

### Examples

#### Example 1

<div class="example-block">
**Input:** l = 8, r = 10

**Output:** 3

**Explanation:**

- 8 and 9 are single-digit integers, so they are good and therefore fancy.

- 10 has digits `[1, 0]`, which form a strictly decreasing sequence, so 10 is good and thus fancy.

Therefore, the answer is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** l = 12340, r = 12341

**Output:** 1

**Explanation:**

- 12340

		<li>12340 is not good because `[1, 2, 3, 4, 0]` is not strictly monotone.

- The digit sum is $1 + 2 + 3 + 4 + 0 = 10$.

- 10 is good as it has digits `[1, 0]`, which is strictly decreasing. Therefore, 12340 is fancy.

	</li>
- 12341

		<li>12341 is not good because `[1, 2, 3, 4, 1]` is not strictly monotone.

- The digit sum is $1 + 2 + 3 + 4 + 1 = 11$.

- 11 is not good as it has digits `[1, 1]`, which is not strictly monotone. Therefore, 12341 is not fancy.

	</li>

Therefore, the answer is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** l = 123456788, r = 123456788

**Output:** 0

**Explanation:**

- 123456788 is not good because its digits are not strictly monotone.

- The digit sum is $1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 8 = 44$.

- 44 is not good as it has digits `[4, 4]`, which is not strictly monotone. Therefore, 123456788 is not fancy.

Therefore, the answer is 0.

</div>
### Constraints

- $1 \le l \le r \le 10^{15}$