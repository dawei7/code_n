## Description

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that $n = 3^x$.
### Function Contract

**Inputs**

- `n`: The signed integer to classify.

**Return value**

Return `True` exactly when `n` is an integral power of three; otherwise return `False`.

### Examples

#### Example 1

- **Input:** $n = 27$
- **Output:** `true`
- **Explanation:** 27 = $3^{3}$
#### Example 2

- **Input:** $n = 0$
- **Output:** `false`
- **Explanation:** There is no x where 3^x = 0.
#### Example 3

- **Input:** $n = -1$
- **Output:** `false`
- **Explanation:** There is no x where 3^x = (-1).
### Constraints

- $-2^{31} \le n \le 2^{31} - 1$

**Follow up:** Could you solve it without loops/recursion?