### 1. Description

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

### 2. Function Contract

**Inputs**

- `num1`: The decimal string for the first non-negative integer.
- `num2`: The decimal string for the second non-negative integer.

**Return value**

Return the exact product of `num1` and `num2` as a decimal string.

### 3. Note

You must not use any built-in BigInteger library or convert the inputs to integer directly.

### 4. Examples

#### Example 1

- **Input:** $num1 = "2", num2 = "3"$
- **Output:** `"6"`
#### Example 2

- **Input:** $num1 = "123", num2 = "456"$
- **Output:** `"56088"`

### 5. Constraints

- $1 \le \text{num1.length}, \text{num2.length} \le 200$

- `num1` and `num2` consist of digits only.

- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.