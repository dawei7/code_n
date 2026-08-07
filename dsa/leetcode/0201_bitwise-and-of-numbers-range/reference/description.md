### 1. Description

Given two integers `left` and `right` that represent the range `[left, right]`, return *the bitwise AND of all numbers in this range, inclusive*.

### 2. Function Contract

**Inputs**

- `left`: The lower endpoint of the inclusive range.
- `right`: The upper endpoint of the inclusive range.

**Return value**

Return $left \& (left + 1) \& ... \& right$.

### 3. Examples

#### Example 1

- **Input:** $left = 5, right = 7$
- **Output:** `4`
#### Example 2

- **Input:** $left = 0, right = 0$
- **Output:** `0`
#### Example 3

- **Input:** $left = 1, right = 2147483647$
- **Output:** `0`

### 4. Constraints

- $0 \le left \le right \le 2^{31} - 1$