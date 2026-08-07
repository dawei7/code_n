## Description

You are given two integer arrays `poly1` and `poly2`, where the element at index `i` in each array represents the coefficient of `x^i` in a polynomial.

Let `A(x)` and `B(x)` be the polynomials represented by `poly1` and `poly2`, respectively.

Return an integer array `result` of length `(poly1.length + poly2.length - 1)` representing the coefficients of the product polynomial `R(x) = A(x) * B(x)`, where `result[i]` denotes the coefficient of `x^i` in `R(x)`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">poly1 = [3,2,5], poly2 = [1,4]</span>

**Output:** <span class="example-io">[3,14,13,20]</span>

**Explanation:**

	- `A(x) = 3 + 2x + 5x^2` and `B(x) = 1 + 4x`

	- `R(x) = (3 + 2x + 5x^2) * (1 + 4x)`

	- `R(x) = 3 * 1 + (3 * 4 + 2 * 1)x + (2 * 4 + 5 * 1)x^2 + (5 * 4)x^3`

	- `R(x) = 3 + 14x + 13x^2 + 20x^3`

	- Thus, result = `[3, 14, 13, 20]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">poly1 = [1,0,-2], poly2 = [-1]</span>

**Output:** <span class="example-io">[-1,0,2]</span>

**Explanation:**

	- `A(x) = 1 + 0x - 2x^2` and `B(x) = -1`

	- `R(x) = (1 + 0x - 2x^2) * (-1)`

	- `R(x) = -1 + 0x + 2x^2`

	- Thus, result = `[-1, 0, 2]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">poly1 = [1,5,-3], poly2 = [-4,2,0]</span>

**Output:** <span class="example-io">[-4,-18,22,-6,0]</span>

**Explanation:**

	- `A(x) = 1 + 5x - 3x^2` and `B(x) = -4 + 2x + 0x^2`

	- `R(x) = (1 + 5x - 3x^2) * (-4 + 2x + 0x^2)`

	- `R(x) = 1 * -4 + (1 * 2 + 5 * -4)x + (5 * 2 + -3 * -4)x^2 + (-3 * 2)x^3 + 0x^4`

	- `R(x) = -4 -18x + 22x^2 -6x^3 + 0x^4`

	- Thus, result = `[-4, -18, 22, -6, 0]`.

</div>

**Constraints:**

	- `1 <= poly1.length, poly2.length <= 5 * 10^4`

	- `-10^3 <= poly1[i], poly2[i] <= 10^3`

	- `poly1` and `poly2` contain at least one non-zero coefficient.
