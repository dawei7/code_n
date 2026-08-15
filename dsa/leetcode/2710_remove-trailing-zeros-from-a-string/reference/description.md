### 1. Description

Given a **positive** integer `num` represented as a string, return *the integer *`num`* without trailing zeros as a string*.

### 2. Function Contract

**Inputs**

- `num`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** $num = "51230100"$
- **Output:** `"512301"`
- **Explanation:** Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".

#### Example 2

- **Input:** $num = "123"$
- **Output:** `"123"`
- **Explanation:** Integer "123" has no trailing zeros, we return integer "123".

### 4. Constraints

- $1 \le \text{num.length} \le 1000$

- `num` consists of only digits.

- `num` doesn't have any leading zeros.
