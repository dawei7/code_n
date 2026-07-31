## Function Contract

**Inputs**

- `expression`: A syntactically valid expression containing integer literals and the four supported binary operations.

There is no whitespace in the grammar. Operands are separated by one comma and enclosed in parentheses after their operator name. Every division has an exact integer result, and all intermediate values fit in a signed long integer.

**Return value**

Return the integer obtained after recursively applying every encoded operation to its two evaluated operands.
