## Description

Given an integer n, return *the **largest palindromic integer** that can be represented as the product of two `n`-digits integers*. Since the answer can be very large, return it **modulo** `1337`.
### Function Contract

**Inputs**

- `n`: the number of decimal digits in each of the two factors

**Return value**

- Return the largest palindromic product of two `n`-digit integers, reduced modulo `1337`.

Determine the largest original palindrome before applying the modulo operation.

### Examples
#### Example 1

- **Input:** $n = 2$
- **Output:** `987`
- **Explanation:** 99 x 91 = 9009, 9009 % 1337 = 987
#### Example 2

- **Input:** $n = 1$
- **Output:** `9`
### Constraints

- $1 \le n \le 8$