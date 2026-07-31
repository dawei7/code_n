## Examples

**Example 1**

- Input: `n = 4104`
- Output: `[1729,4104]`
- Explanation: Exactly two good integers do not exceed $4104$:

  - $1729=1^3+12^3=9^3+10^3$, using the distinct pairs $(1,12)$ and $(9,10)$.
  - $4104=2^3+16^3=9^3+15^3$, using the distinct pairs $(2,16)$ and $(9,15)$.

  Therefore the ascending result is `[1729,4104]`.

**Example 2**

- Input: `n = 578`
- Output: `[]`
- Explanation: No integer at most $578$ has two distinct representations of the required form, so the result is empty.
