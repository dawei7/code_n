## General
**Reduce each side to two integers**

Every side has the form `coefficient * x + constant`. Scan its terms from left to right, reading an optional sign, then an optional decimal magnitude, and finally whether the term ends in `x`. A bare `x` has magnitude one; signed constants contribute only to the constant total.

**Move like terms across the equality**

If the sides reduce to `left_coefficient * x + left_constant` and `right_coefficient * x + right_constant`, rearrangement gives `(left_coefficient - right_coefficient) * x = right_constant - left_constant`.

**Classify cancellation before division**

When the combined coefficient is zero, a zero combined constant means the equality holds for every `x`; a nonzero constant means it can never hold. Otherwise the contract guarantees an integer unique solution, obtained by dividing the combined constant by the combined coefficient.

**Why symbolic aggregation preserves the equation**

The parser adds every signed `x` term to exactly one coefficient and every signed numeric term to exactly one constant. Addition is associative, so regrouping those terms does not change either side. Subtracting the right totals from both sides is an equivalent transformation, and the final classification exhausts the zero- and nonzero-coefficient cases.

## Complexity detail
Each of the `N` equation characters is scanned once and decimal digits are accumulated in place, giving $O(N)$ time. A constant number of coefficients, constants, signs, and indices uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Tokenize with regular expressions:** can produce the same signed terms concisely, but allocates token strings and depends on careful handling of bare `x`.
- **Brute-force candidate values:** repeatedly evaluates the equation until a match is found; it is correct for a bounded search but can be much slower than direct algebra.
- **General expression parser:** supports richer grammars but is unnecessary for a linear, parenthesis-free contract.
- A bare `x`, `+x`, or `-x` has coefficient `1`, `1`, or `-1`.
- A unique solution may be zero or negative.
- Equal coefficients with unequal constants produce no solution.
- Equal coefficients and equal constants produce infinitely many solutions.
- Multi-digit coefficients and constants must be read as whole numbers rather than individual digits.
