## General
**Every bit position follows the same three-state counter**

For each bit independently, only its count modulo three matters. Encode state zero as absence from both masks, state one as membership in `ones`, and state two as membership in `twos`. The masks operate on all integer bit positions in parallel.

**Ordered Boolean updates implement `0 -> 1 -> 2 -> 0`**

For each value, update:

```text
ones = (ones XOR value) AND NOT twos
twos = (twos XOR value) AND NOT ones
```

The second expression intentionally uses the newly updated `ones`. For a current input bit of one, a state-zero bit enters `ones`; a state-one bit leaves `ones` and enters `twos`; a state-two bit is blocked from `ones` and toggled out of `twos`. A current input bit of zero leaves its state unchanged.

Masking against the other register keeps `ones` and `twos` disjoint, so the impossible “both set” encoding never appears.

**Masks equal the processed bit-frequency residues**

For every bit position, membership in `ones` or `twos` exactly represents its total occurrence count modulo three across the processed prefix.

**Trace one bit through three repeated occurrences**

Suppose a repeated number has some bit set. Its first occurrence places that bit in `ones`; its second moves it to `twos`; its third clears it from both. The unique number contributes its set bits only once, so after every triple has completed, exactly its bit pattern remains in `ones`.

**Each bit cycles through counts modulo three**

For every bit position, membership in neither mask, `ones`, or `twos` represents occurrence count zero, one, or two modulo three. The mask updates advance a set input bit through those states and return it to neither mask on the third occurrence.

Every tripled value therefore contributes zero modulo three at every position. The unique value contributes once, leaving exactly its set bits in `ones`, including the fixed-width sign bit representation.

## Complexity detail
Each of `n` values performs constant bitwise work, giving $O(n)$ time. Two integer masks use $O(1)$ space.

## Alternatives and edge cases
- **Count each fixed-width bit:** is also linear with constant space but requires explicit signed conversion.
- **Frequency map:** is simpler but uses $O(n)$ space.
- **Plain XOR:** is insufficient because $x \oplus x \oplus x = x$, so triple values do not cancel.
- Zero and negative integers obey the same mask transitions.
- A one-element array leaves that value directly in `ones`.
- In languages with fixed-width integers, the masks naturally preserve the unique signed bit pattern. Language-specific arbitrary-width signed bit operations should be verified against the platform semantics.
