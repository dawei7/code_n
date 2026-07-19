## General
**Every digit pair has a predetermined place-value position**

The product of an `m`-digit and `n`-digit number has at most $m + n$ digits. Allocate that many integer slots. If input digits at indices `i` and `j` are multiplied, their units contribution belongs at result index $i + j + 1$, and carry flows to $i + j$. This index relationship is the array form of decimal place values.

**Accumulate and normalize from right to left**

Process both strings from right to left. Convert individual digit characters only, multiply them, and add the product to the existing value in the lower result slot. Store the sum's units digit there and add its carry to the preceding slot. Later digit pairs naturally incorporate carry accumulated at their lower slot and normalize it in turn.

After all pairs, skip leading zero slots and join the remaining digits. Handle a zero operand immediately.

**Deferred higher carries still preserve the represented value**

After pair `(i, j)` is processed, its exact place-value contribution has been added to the two corresponding result slots, and the lower slot is normalized to one decimal digit. A higher slot may temporarily exceed nine, but that does not lose value: it becomes the lower slot of a later more-significant pair and is then split into digit and carry. Contributions from not-yet-processed pairs remain absent.

**Trace place-value accumulation**

For `12 × 34`, digit products are `2×4`, `2×3`, `1×4`, and `1×3`. Adding them at their place-value positions with carries produces slots representing `0408`, which normalize and trim to `408`.

**Every digit pair contributes to one exact place value**

Writing both operands as sums of digit times powers of ten, distributivity expands their product into one term for every digit pair. The nested loops enumerate each pair once and add its product to the slot for the sum of their decimal positions.

Carry propagation replaces an oversized slot by an equivalent remainder digit plus tens transferred to the next slot, preserving the represented integer. After all slots are normalized, they encode the exact product. Trimming only unused leading zero slots changes no value and produces the canonical decimal spelling.

## Complexity detail
All `m × n` digit pairs are multiplied once, so time is $O(mn)$. The result array contains $m + n$ integer slots and the final string has the same order of size, giving $O(m + n)$ space.

## Alternatives and edge cases
- **Convert complete strings to integers:** violates the contract and may overflow fixed-width languages.
- **Repeated addition:** can require work proportional to an operand's numeric value rather than its digit length.
- **Karatsuba or FFT multiplication:** improves asymptotics for very large strings but is excessive for the bounded input sizes here.
- If either operand is exactly `"0"`, return `"0"` immediately. Trimming all leading zero slots must still leave one zero for a zero product.
- The contract excludes signs, decimal points, and noncanonical leading zeroes, so the simulation handles only decimal digit characters.
