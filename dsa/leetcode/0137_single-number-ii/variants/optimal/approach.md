## General
**Two masks encode every bit count modulo three**

Treat each bit position independently while updating all positions in parallel. A bit absent from both masks has residue zero, a bit in `ones` has residue one, and a bit in `twos` has residue two. The two masks remain disjoint, so these are the only reachable states.

For each `value`, update `ones` with `(ones ^ value) & ~twos`, then update `twos` with `(twos ^ value) & ~ones`. The second expression deliberately uses the new `ones`. For an input bit equal to one, these ordered updates advance its state through zero, one, two, and back to zero; an input bit equal to zero leaves the state unchanged.

**Every triple disappears and the singleton remains**

After any processed prefix, the masks represent every bit's occurrence count modulo three. Each value that appears three times therefore returns all of its set bits to residue zero. The unique value advances its set bits only once, so its complete bit pattern remains in `ones` after the scan. Python's signed bitwise operations preserve the same cancellation property for negative integers, because equal signed values undergo identical transitions.

## Complexity detail
Each of the $n$ values performs a constant number of bitwise operations, giving $O(n)$ time. `ones` and `twos` are the only algorithmic state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Count each fixed-width bit modulo three:** also meets the bounds but needs explicit reconstruction of a negative signed result.
- **Frequency map:** is simpler but requires $O(n)$ extra space.
- **Sort and inspect runs:** costs $O(n \log n)$ time and may mutate the input.
- **Plain XOR:** does not cancel triples because $x \oplus x \oplus x = x$.
- Zero and negative values follow the same mask transitions, and a one-element array leaves its sole value in `ones`.
- The state machine is specific to multiplicity three; other repetition counts require different residue logic.
