## General
**Treat each bit position independently**

Bitwise OR has no carry between positions. At one position, let `a_bit`, `b_bit`, and `c_bit` be the corresponding bits. Choices made there cannot affect any other position, so an optimal global answer is the sum of the minimum costs for the individual positions.

**Count the forced changes**

If `c_bit` is 0, both input bits must end as 0. The local cost is therefore `a_bit + b_bit`: each present 1 must be cleared.

If `c_bit` is 1, at least one input bit must end as 1. The cost is 0 when either input bit is already 1, and otherwise exactly 1 because either zero can be flipped. These are all possible three-bit configurations, so summing their local optima gives the minimum total.

Process the least-significant bits, shift all three values right, and continue until every remaining value is zero. This includes leading positions that occur in only one of the three original values.

## Complexity detail
The loop examines one position for each bit of $M$, or $O(\log M)$ positions. It stores only the shifted integers, their current bits, and the running total, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Bit-count identity:** Masks for unwanted 1s and missing 1s can be combined with population counts for a compact solution, but the per-bit cases make the minimum argument more explicit.
- **Binary strings:** Padding three strings to the same length also works in $O(\log M)$ time but allocates $O(\log M)$ additional space.
- **Target bit 0 with two input 1s:** Both 1s must be cleared, so that position contributes 2 rather than 1.
- **Target bit 1 with two input 0s:** Flipping either input is sufficient, so the position contributes exactly 1.
- **Already equal:** If `a | b` is `c`, every bit contributes 0.
- **Different bit lengths:** Continue through bits present in any of the three values; stopping when only one shifted value becomes zero would miss required changes.
