## Function Contract

**Inputs**

- `mat`: A rectangular matrix of positive integers; exactly one position must be selected from each row.

Choices are based on cell positions. If the same value occurs more than once in a row, selecting either occurrence represents a different way even though it contributes the same integer to the GCD.

**Return value**

Return the number of row-by-row selections whose overall greatest common divisor equals `1`, reduced modulo $1{,}000{,}000{,}007$.
