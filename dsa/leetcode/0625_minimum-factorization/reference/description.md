## Description

Given a positive integer num, return *the smallest positive integer *`x`* whose multiplication of each digit equals *`num`. If there is no answer or the answer is not fit in **32-bit** signed integer, return `0`.
### Function Contract

**Inputs**

- `a`: The positive digit-product target called `num` in the source statement.

**Return value**

Return the smallest positive integer whose decimal digits multiply to `a`. Return `0` when no such positive integer exists or when the smallest valid result is greater than $2^{31} - 1$.

### Examples

#### Example 1

- **Input:** $num = 48$
- **Output:** `68`
#### Example 2

- **Input:** $num = 15$
- **Output:** `35`
### Constraints

- $1 \le num \le 2^{31} - 1$