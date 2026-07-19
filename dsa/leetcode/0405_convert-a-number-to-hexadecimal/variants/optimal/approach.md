## General
**Normalize to the unsigned 32-bit pattern**

Mask `num` with `0xffffffff`. Positive values are unchanged, while a negative Python integer becomes the same finite 32-bit bit pattern used by fixed-width two's-complement arithmetic.

**Translate one low nibble at a time**

The lowest four bits form one hexadecimal digit from zero through fifteen. Use that value to index `"0123456789abcdef"`, append the character, and shift the working value right by four bits.

**Reverse the collected digits**

Low nibbles are extracted from least significant to most significant, so reverse the character list at the end. Stopping when the remaining value is zero omits leading zeroes naturally; handle original zero separately so its representation is not empty.

**Why negative values produce eight digits**

After masking, a negative signed value has a nonzero high bit in a 32-bit unsigned pattern. Exactly eight four-bit extractions consume all 32 bits. Each extraction preserves the remaining higher bits, so their reversed digits are precisely the standard two's-complement hexadecimal form.

## Complexity detail
A 32-bit value contains at most eight hexadecimal digits, so the loop performs at most eight iterations and uses at most eight temporary characters. Both time and auxiliary space are $O(1)$ for the fixed-width contract.

## Alternatives and edge cases
- **Repeated division by sixteen:** is equivalent for nonnegative values but still requires explicit two's-complement normalization for negatives.
- **Language formatting helpers:** are concise but bypass the intended bit conversion and may include prefixes or signed formatting.
- **Prepend immutable characters:** is harmless at eight digits but would copy repeatedly for an unbounded-width generalization.
- Zero must return one digit rather than an empty string.
- Values from zero through fifteen produce one hexadecimal digit.
- The minimum signed integer becomes `80000000`.
- No `0x` prefix or uppercase letters belong in the result.
