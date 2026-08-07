## Description

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses **substring*.
### Function Contract

**Inputs**

- `s`: The parenthesis string to examine.

**Return value**

Return the maximum length of a well-formed parenthesis substring.

### Examples

#### Example 1

- **Input:** `s = "(()"`
- **Output:** `2`
- **Explanation:** The longest valid parentheses substring is "()".
#### Example 2

- **Input:** `s = ")()())"`
- **Output:** `4`
- **Explanation:** The longest valid parentheses substring is "()()".
#### Example 3

- **Input:** `s = ""`
- **Output:** `0`
### Constraints

- $0 \le \text{s.length} \le 3 * 10^{4}$

- $s[i]$ is `'('`, or `')'`.