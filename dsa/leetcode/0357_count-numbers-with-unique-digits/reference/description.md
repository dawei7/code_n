### 1. Description

Given an integer `n`, return the count of all numbers with unique digits, `x`, where $0 \le x < 10^n$.

### 2. Function Contract

**Inputs**

- `n`: The exponent defining the exclusive upper bound $10^n$.

**Return value**

Return the number of integers in $[0,10^n)$ that contain no repeated decimal digit.

### 3. Examples

#### Example 1

- **Input:** $n = 2$
- **Output:** `91`
- **Explanation:** The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

#### Example 2

- **Input:** $n = 0$
- **Output:** `1`

### 4. Constraints

- $0 \le n \le 8$
