## Function Contract

**Inputs**

- `s`: A parenthesis string to reduce.
- `k`: The number of consecutive opening parentheses and consecutive closing parentheses in the removable pattern.

The removable substring has length `2 * k` and is exactly `'(' * k + ')' * k`. Removals may create new occurrences across the newly joined boundary, so processing continues to a fixed point.

**Return value**

Return the unreduced characters, in their original relative order, after no k-balanced substring remains.
