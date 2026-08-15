### 1. Description

You are given a positive integer `n`, you can do the following operation **any** number of times:

- Add or subtract a **power** of `2` from `n`.

Return *the **minimum** number of operations to make *`n`* equal to *`0`.

A number `x` is power of `2` if $x = 2^i$ where $i \ge 0$*.*

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $n = 39$
- **Output:** `3`
- **Explanation:** We can do the following operations:
- Add $2^{0}$ = 1 to n, so now n = 40.
- Subtract $2^{3}$ = 8 from n, so now n = 32.
- Subtract $2^{5}$ = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.

#### Example 2

- **Input:** $n = 54$
- **Output:** `3`
- **Explanation:** We can do the following operations:
- Add $2^{1}$ = 2 to n, so now n = 56.
- Add $2^{3}$ = 8 to n, so now n = 64.
- Subtract $2^{6}$ = 64 from n, so now n = 0.
So the minimum number of operations is 3.

### 4. Constraints

- $1 \le n \le 10^{5}$
