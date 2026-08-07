## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.

- Open brackets must be closed in the correct order.

- Every close bracket has a corresponding open bracket of the same type.
### Function Contract

**Inputs**

- `s`: The non-empty bracket string to validate.

**Return value**

Return `True` when every bracket is correctly matched and nested; otherwise return `False`.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "()"

**Output:** true

</div>
#### Example 2

<div class="example-block">
**Input:** s = "()[]{}"

**Output:** true

</div>
#### Example 3

<div class="example-block">
**Input:** s = "(]"

**Output:** false

</div>
#### Example 4

<div class="example-block">
**Input:** s = "([])"

**Output:** true

</div>
#### Example 5

<div class="example-block">
**Input:** s = "([)]"

**Output:** false

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of parentheses only `'()[]{}'`.