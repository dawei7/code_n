### 1. Description

Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates `x` raised to the power `n` (i.e., $x^n$).

### 2. Function Contract

**Inputs**

- `x`: The real-valued base.
- `n`: The integer exponent.

**Return value**

Return $x^n$ as a floating-point number.

### 3. Examples

#### Example 1

- **Input:** $x = 2.00000, n = 10$
- **Output:** `1024.00000`
#### Example 2

- **Input:** $x = 2.10000, n = 3$
- **Output:** `9.26100`
#### Example 3

- **Input:** $x = 2.00000, n = -2$
- **Output:** `0.25000`
- **Explanation:** $2^{-2}$ = 1/$2^{2}$ = 1/4 = 0.25

### 4. Constraints

- `-100.0 < x < 100.0`

- $-2^{31} \le n \le 2^{31}-1$

- `n` is an integer.

- Either `x` is not zero or `n > 0`.

- $-10^{4} \le x^n \le 10^{4}$