## Function Contract

**Inputs**

- `equations`: Variable-name pairs describing known divisions.
- `values`: The positive real quotient corresponding to each equation.
- `queries`: Variable-name pairs whose quotients must be evaluated.

**Return value**

Return the quotient for each query in order, using `-1.0` when either variable is undefined or no relationship determines the quotient.
