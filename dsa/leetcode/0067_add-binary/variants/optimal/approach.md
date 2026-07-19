## General
**Align the strings at their least significant ends**

Keep one index at the end of each string and a carry. At every step, start with the carry, add each input bit whose index is still valid, append `total % 2`, and update the carry to `floor(total / 2)`. Independent indices naturally handle unequal input lengths without left-padding either string.

**The final carry is another binary column**

The loop ends only when both indices are exhausted and the carry is zero. If both inputs end with a carry of one, that carry supplies the new most-significant bit. The produced bits are least-significant first, so reverse the buffer once rather than repeatedly prepending.

**Low-order result bits become final immediately**

After each iteration, the output buffer contains the correct low-order bits of $a + b$ in reverse order, and `carry` is precisely the value transferred into the next unprocessed column.

**Trace a carry through unequal strings**

For $1010 + 1011$, the rightmost columns produce bits `1,0,1,0` with carries propagated through the middle; a final carry supplies the leading 1. Reversing the buffer yields `10101`.

**Remainder and quotient exactly split each binary column**

For two current bits plus the incoming carry, `total % 2` is the unique bit occupying that binary position and `floor(total / 2)` is the complete carry into the next position. This identity preserves the numeric value of the processed columns.

Moving from least to most significant applies the same exact decomposition at every position. Once both inputs and the final carry are exhausted, all place values have been accounted for; reversing the collected low-to-high bits yields the complete binary sum.

## Complexity detail
The loop runs once per position of the longer input plus at most one carry, giving $O(\max(m,n))$ time. The returned character buffer uses the same order of space.

## Alternatives and edge cases
- **Parse both strings as integers:** may overflow, trigger arbitrary-length conversion limits, or bypass the intended algorithm.
- **Prepend each result bit:** preserves display order but can make immutable-string construction quadratic.
- **Recursive column addition:** is correct but uses linear call-stack space in addition to the output.
- Adding `"0"` preserves the other canonical input. Two all-one suffixes may propagate a carry across the complete longer string.
- Convert only individual characters to bit values; converting either complete input defeats the arbitrary-length purpose.
