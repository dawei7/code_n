### 1. Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.

- Open brackets must be closed in the correct order.

- Every close bracket has a corresponding open bracket of the same type.

### 2. Function Contract

**Inputs**

- `s`: The non-empty bracket string to validate.

**Return value**

Return `True` when every bracket is correctly matched and nested; otherwise return `False`.

### 3. Examples

#### Example 1

- **Input:** s = "()"

- **Output:** true

#### Example 2

- **Input:** s = "()[]{}"

- **Output:** true

#### Example 3

- **Input:** s = "(]"

- **Output:** false

#### Example 4

- **Input:** s = "([])"

- **Output:** true

#### Example 5

- **Input:** s = "([)]"

- **Output:** false

### 4. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of parentheses only `'()[]{}'`.
