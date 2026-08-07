### 1. Description

You are given an integer `n`.

Form a new integer `x` by concatenating all the **non-zero digits** of `n` in their original order. If there are no **non-zero** digits, $x = 0$.

Let `sum` be the **sum of digits** in `x`.

Return an integer representing the value of $x * sum$.

### 2. Function Contract

**Inputs**

- `n`: The nonnegative integer whose decimal digits are filtered.

Let $D$ be the number of decimal digits in `n`, treating `0` as a one-digit representation. Removing zeros must preserve the relative order of every retained digit.

**Return value**

Return the concatenation of all nonzero digits multiplied by the sum of those same digits. If there are no retained digits, both the concatenated value and the result are `0`.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 10203004

**Output:** 12340

**Explanation:**

- The non-zero digits are 1, 2, 3, and 4. Thus, $x = 1234$.

- The sum of digits is $sum = 1 + 2 + 3 + 4 = 10$.

- Therefore, the answer is $x * sum = 1234 * 10 = 12340$.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1000

**Output:** 1

**Explanation:**

- The non-zero digit is 1, so $x = 1$ and $sum = 1$.

- Therefore, the answer is $x * sum = 1 * 1 = 1$.

</div>

### 4. Constraints

- $0 \le n \le 10^{9}$