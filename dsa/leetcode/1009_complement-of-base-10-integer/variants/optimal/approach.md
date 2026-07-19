## General
**Build a mask over exactly the significant bits:** Start with `mask = 1` and repeatedly shift it left while it is no greater than `n`. When the loop stops, `mask` is the first power of two larger than `n`; subtracting one produces $B$ consecutive `1` bits.

**Flip only the represented positions:** XOR `n` with `mask - 1`. A `1` in every mask position toggles the corresponding significant bit, while no higher position is touched. Thus `1010 XOR 1111` becomes `0101`.

**Give zero its one-bit representation:** For `n == 0`, the shifting loop would leave `mask - 1` equal to zero. Return `1` directly because the source representation is `0`, not an empty bit string.

The mask contains a `1` in precisely every position written in `n` and nowhere else. XOR therefore flips every required bit exactly once without introducing a leading complemented bit.

## Complexity detail
The mask advances once per significant bit, taking $O(B)$ time. A constant number of integer variables gives $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Use the bit length directly:** `(1 << n.bit_length()) - 1` forms the mask compactly when the language exposes that operation.
- **Convert to a binary string:** Replacing characters is straightforward but allocates $O(B)$ additional space.
- **Recompute every positional power:** Building each complemented bit's value from scratch is correct but can take $O(B^2)$ time.
- **Zero:** Its one displayed bit flips from `0` to `1`.
- **All bits are one:** The complement is zero, as with `n = 7`.
