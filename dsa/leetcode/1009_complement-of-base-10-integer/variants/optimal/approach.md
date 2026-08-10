## General

**Flip only the bits that belong to the ordinary binary representation**

Positive integers conceptually have infinitely many leading zero bits, but those leading zeros are not written in the standard binary representation and must not be complemented. For example, five is `101`, not `000...0101`, so only its three significant positions are flipped.

The algorithm processes bits from least significant to most significant and stops once all original significant bits have been consumed.

**Handle zero separately**

Zero's ordinary binary representation is `"0"`, whose complement is `"1"`, or decimal one.

The main loop uses `while n`. If `n` were initially zero, it would run zero times and leave `ans = 0`, which would be wrong. The explicit base case returns one before the loop.

This is the only input whose significant representation contains a bit even though right-shifting the numeric value offers no loop iteration.

**Extract and flip the current bit**

At each iteration:

`n & 1`

extracts the least significant bit. AND with one clears every higher position and leaves either zero or one.

XOR with one flips that bit:

- `0 ^ 1 = 1`;
- `1 ^ 1 = 0`.

Conceptually, the subexpression is `(n & 1) ^ 1`. It produces the complement bit for the current position.

**Place the flipped bit into the answer**

Variable `i` is the zero-based bit position currently being processed. Shifting the complemented bit left by `i` moves it into that position:

`((n & 1) ^ 1) << i`.

The OR assignment

`ans |= ...`

sets that answer bit when the complement is one and leaves all previously constructed positions unchanged. When the complement bit is zero, OR with zero has no effect, which is exactly correct because `ans` began with all bits clear.

**Advance to the next source bit**

After processing one position:

- `i += 1` advances the destination position;
- `n >>= 1` discards the source bit just processed and moves the next bit into the least significant position.

Because the input is nonnegative, right shift fills from the left with zeros. After exactly `B` iterations, where `B` is the original bit length, `n` becomes zero and the loop ends.

No leading zero positions are processed, so they are not incorrectly turned into leading ones.

**Trace `n = 10`**

Ten is binary `1010`. Process from right to left:

- Source bit zero at position zero flips to one, so `ans` gains `0001`.
- Source bit one at position one flips to zero.
- Source bit zero at position two flips to one, so `ans` gains `0100`.
- Source bit one at position three flips to zero.

The final answer bits are `0101`, which equal decimal five.

For seven, all three source bits are one, so all complement bits are zero and `ans` remains zero.

**The bit-position invariant**

Before each iteration at position `i`:

- the lower `i` positions of `ans` are exactly the complements of the lower `i` bits of the original input;
- current `n` equals the original input shifted right by `i`;
- no higher answer position has been set.

Extracting, flipping, and shifting the current least significant bit establishes the next answer position. Advancing `i` and right-shifting `n` preserves the invariant.

When `n` becomes zero, all and only original significant bits have been processed. Therefore, `ans` is exactly the requested complement.

**Why bitwise NOT alone is unsuitable**

In Python, `~n` represents the infinite-width two's-complement NOT and equals `-n - 1`. It flips conceptual leading zeros too, producing a negative integer for nonnegative `n`.

The explicit significant-bit loop avoids any fixed-width assumption and returns the intended nonnegative value.

**The local reassignment of `n` is safe**

The method repeatedly shifts parameter `n` until it becomes zero. Python passes the integer object reference into a local parameter binding, and integers are immutable. Reassigning the local name does not alter a caller-owned variable.

## Complexity detail

Let `B` be the number of bits in the binary representation of the original positive input.

The loop executes exactly `B` times and performs constant-time bit operations per position under the usual word-level model, so time complexity is `O(B)`. With the stated bound below one billion, `B <= 30`.

Only `ans`, `i`, and the shifted local `n` are stored, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Same-length all-ones mask:** Compute `mask = (1 << n.bit_length()) - 1` and return `mask ^ n`. It flips all significant positions at once.
- **Subtract from the mask:** For an all-ones mask of the same bit length, `mask - n` also equals the complement.
- **Propagate the highest one bit:** Repeated OR-with-shift operations can turn every bit below the highest one into a mask, then XOR with `n`.
- **Binary-string conversion:** Map each `0` to `1` and each `1` to `0`, then parse. It is clear but allocates text and extra storage.
- **Bitwise NOT:** Produces a negative two's-complement value unless explicitly masked, so using it alone is incorrect.
- **`n = 0`:** Requires the explicit result one because the loop would otherwise process no bits.
- **All one bits:** Values such as seven complement to zero.
- **Power of two:** A representation such as `1000` becomes `0111`, one less than the original power.
- **Leading zeros:** They are not part of the representation and are deliberately never visited.
- **Maximum input:** Fewer than thirty-one loop iterations are needed.
