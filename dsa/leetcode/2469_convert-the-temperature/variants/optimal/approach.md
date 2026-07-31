## General

The input already represents a Celsius temperature, so no parsing or search is needed. Compute Kelvin by shifting the Celsius scale upward by $273.15$. Compute Fahrenheit by scaling the Celsius value by $1.8$ and then adding $32$.

Return the two results in the contract's required order: Kelvin first and Fahrenheit second. Each formula is a direct definition of the target scale, so the resulting entries are exactly the requested conversions up to ordinary floating-point representation error covered by the accepted tolerance.

## Complexity detail

The input has fixed arity and the method performs a fixed number of arithmetic operations, giving $O(1)$ time.

The returned array always has two elements and no variable-sized auxiliary structure is used, giving $O(1)$ space.

## Alternatives and edge cases

- **Inline both formulas:** Returning both expressions directly is equivalent; named values make the required output order easier to verify.
- **Decimal arithmetic:** Exact decimal types can represent the stated hundredths precisely, but binary floating point already satisfies the $10^{-5}$ acceptance tolerance.
- **Output order:** Kelvin must precede Fahrenheit; reversing two correct values still violates the contract.
- **Zero Celsius:** The lower bound converts to $273.15$ Kelvin and $32$ Fahrenheit.
- **Upper bound:** The same formulas apply directly at `celsius = 1000` without overflow or special handling.
- **Fractional values:** Preserve the floating-point result rather than rounding it to a fixed number of displayed decimal places.
