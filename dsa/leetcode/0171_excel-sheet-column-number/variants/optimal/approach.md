## General
Interpret the title as a positional numeral with base 26 and digit values $A = 1$ through $Z = 26$. Although this alphabet has no zero digit, left-to-right evaluation works like an ordinary base representation once each character has been mapped to its one-based value.

Maintain a running `total`. For each letter with value `digit`, update

`total = total * 26 + digit`.

Multiplication shifts the previously processed prefix one position to the left, and addition installs the new least-significant digit. This is Horner's rule applied to the title's positional polynomial.

For `"ZY"`, processing `Z` gives `26`; processing `Y` gives $26 \cdot 26 + 25 = 701$. For `"AB"`, the calculation is $1 \cdot 26 + 2 = 28$, explaining why `AA` begins at 27 rather than at 26.

After processing any prefix, `total` equals the numeric value represented by that prefix. This is true for the empty prefix, whose value is zero. Appending a letter shifts every existing digit one base-26 position and adds the new digit, exactly the update `26 * total + digit`; therefore the property is preserved. By induction, after the final character, `total` is the value of the complete column title.

## Complexity detail
Each of the `n` characters is converted and accumulated once, so time is $O(n)$. The running total and current digit use $O(1)$ auxiliary space.

## Alternatives and edge cases
- Explicitly summing `digit * 26 ^ position` is correct but requires powers and more bookkeeping than Horner's rule.
- Mapping `A` to zero produces incorrect values because Excel's notation is bijective and has no zero symbol.
- Generating titles until the input is reached takes time proportional to the numeric answer instead of the title length.
- Single letters map to `1..26`; `AA`, `ZZ`, and `AAA` are useful boundary tests.
- Fixed-width languages should ensure the accumulator type can hold the maximum permitted result.
