## General

**Make every adjacent pair visible at once.** Shifting `n` one position to the right aligns each original bit with the bit immediately above it. Therefore, in

`adjacent_pairs = n & (n >> 1)`,

bit $i$ is set exactly when original bits $i$ and $i+1$ are both set. Each adjacent `11` occurrence has one unique lower position, so the number of set bits in `adjacent_pairs` is precisely the number of adjacent set-bit pairs. This also counts overlapping pairs correctly: for `111`, the mask contains two set bits.

**Recognize a one-bit mask.** For any positive integer $x$, clearing its lowest set bit with `x & (x - 1)` produces zero exactly when $x$ originally had one set bit. Requiring `adjacent_pairs != 0` excludes the no-pair case. Consequently, the returned condition is true exactly when the binary representation contains one adjacent set-bit pair.

## Complexity detail

The legal input is at most $10^5$ and therefore occupies at most 17 binary positions. The accepted method performs a fixed number of integer shifts, bitwise operations, comparisons, and one subtraction, so it takes $O(1)$ time and $O(1)$ auxiliary space under the repository's fixed-width integer model.

Because the complete legal domain contains only 100,001 values and never exceeds 17 bits, runtime scaling cannot honestly distinguish plausible bit-processing classes. Complexity verification therefore uses a strict `bounded_domain` certificate backed by a fixed-operation proof and an exhaustive comparison of every legal value against an independent binary-string oracle.

## Alternatives and edge cases

- **Binary-string scan:** Convert `n` to binary and count adjacent `11` windows directly. This mirrors the statement and takes $O(B)$ time and $O(B)$ space for $B$ binary digits, but the mask identity avoids the allocation.
- **Bit-by-bit simulation:** Track the previous bit while shifting through `n`. It uses $O(1)$ space and $O(B)$ time, but must continue after finding the first pair so that a second pair is not missed.
- **No pair:** Zero, powers of two, and alternating representations leave `adjacent_pairs` equal to zero and must return `false`.
- **Overlapping pairs:** A run such as `111` produces two marked positions, so it correctly returns `false`.
- **Separated pairs:** A representation such as `11011` also produces two marked positions even though the pairs do not overlap.
- **Exactly one pair:** Extra isolated set bits do not affect the one-bit mask and therefore do not change a valid result.
