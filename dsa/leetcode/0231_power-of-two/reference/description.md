### 1. Description

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that $n = 2^x$.

### 2. Function Contract

**Inputs**

- `n`: The signed integer to classify.

**Return value**

Return `true` exactly when `n` equals $2^x$ for some integer `x`; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** $n = 1$
- **Output:** `true`
- **Explanation:** $2^{0}$ = 1

#### Example 2

- **Input:** $n = 16$
- **Output:** `true`
- **Explanation:** $2^{4}$ = 16

#### Example 3

- **Input:** $n = 3$
- **Output:** `false`

### 4. Constraints

- $-2^{31} \le n \le 2^{31} - 1$

**Follow up:** Could you solve it without loops/recursion?
