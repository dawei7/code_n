### 1. Description

Given an integer `n`, return *`true` if it is a power of four. Otherwise, return `false`*.

An integer `n` is a power of four, if there exists an integer `x` such that $n = 4^x$.

### 2. Function Contract

**Inputs**

- `n`: The signed 32-bit integer to classify.

**Return value**

Return `true` exactly when `n` equals an integer power of four; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** $n = 16$
- **Output:** `true`
#### Example 2

- **Input:** $n = 5$
- **Output:** `false`
#### Example 3

- **Input:** $n = 1$
- **Output:** `true`

### 4. Constraints

- $-2^{31} \le n \le 2^{31} - 1$

**Follow up:** Could you solve it without loops/recursion?