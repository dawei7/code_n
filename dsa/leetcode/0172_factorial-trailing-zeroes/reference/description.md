## Description

Given an integer `n`, return *the number of trailing zeroes in *`n!`.

Note that $n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1$.
### Function Contract

**Inputs**

- `n`: A nonnegative integer.

**Return value**

Return the number of zero digits at the end of the decimal representation of `n!`.

### Examples
#### Example 1

- **Input:** $n = 3$
- **Output:** `0`
- **Explanation:** 3! = 6, no trailing zero.
#### Example 2

- **Input:** $n = 5$
- **Output:** `1`
- **Explanation:** 5! = 120, one trailing zero.
#### Example 3

- **Input:** $n = 0$
- **Output:** `0`
### Constraints

- $0 \le n \le 10^{4}$

**Follow up:** Could you write a solution that works in logarithmic time complexity?