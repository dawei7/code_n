### 1. Description

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return *the result of the evaluation*.

### 2. Function Contract

**Inputs**

- `s`: A valid expression containing integers, addition, subtraction, parentheses, and spaces.

**Return value**

Return the integer value of the complete expression.

### 3. Note

You are **not** allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

### 4. Examples

#### Example 1

- **Input:** `s = "1 + 1"`
- **Output:** `2`

#### Example 2

- **Input:** `s = " 2-1 + 2 "`
- **Output:** `3`

#### Example 3

- **Input:** `s = "(1+(4+5+2)-3)+(6+8)"`
- **Output:** `23`

### 5. Constraints

- $1 \le \text{s.length} \le 3 * 10^{5}$

- `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.

- `s` represents a valid expression.

- `'+'` is **not** used as a unary operation (i.e., `"+1"` and $"+(2 + 3)"$ is invalid).

- `'-'` could be used as a unary operation (i.e., `"-1"` and $"-(2 + 3)"$ is valid).

- There will be no two consecutive operators in the input.

- Every number and running calculation will fit in a signed 32-bit integer.
