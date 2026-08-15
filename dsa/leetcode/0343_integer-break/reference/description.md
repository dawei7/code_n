### 1. Description

Given an integer `n`, break it into the sum of `k` **positive integers**, where $k \ge 2$, and maximize the product of those integers.

Return *the maximum product you can get*.

### 2. Function Contract

**Inputs**

- `n`: The integer that must be split into at least two positive parts.

**Return value**

Return the maximum product of the positive integers in a valid sum decomposition of `n`.

### 3. Examples

#### Example 1

- **Input:** $n = 2$
- **Output:** `1`
- **Explanation:** 2 = 1 + 1, 1 × 1 = 1.

#### Example 2

- **Input:** $n = 10$
- **Output:** `36`
- **Explanation:** 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

### 4. Constraints

- $2 \le n \le 58$
