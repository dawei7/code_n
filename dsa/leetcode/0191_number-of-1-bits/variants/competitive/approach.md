## General

**Compute many local counts in parallel**

The selected competitive `Solution` uses a SWAR-style population count:
“SIMD within a register.” Instead of examining one position per iteration, it
stores counts inside groups of bits and repeatedly combines adjacent groups.
Five fixed mask-and-add stages grow group width from one bit to 2, 4, 8, 16,
and finally 32 bits.

At every stage, each group contains the number of original 1-bits in the
corresponding portion of the input. The last 32-bit group therefore contains
the total Hamming weight.

**First stage: count each adjacent pair**

Mask `0x55555555` has binary pattern `0101` repeated across 32 positions. The
expression `n & 0x55555555` selects the lower-positioned bit from every 2-bit
pair. Shifting `n` right by one moves each pair's upper bit into that lower
position, and applying the same mask selects it.

Adding the two masked values produces, inside each 2-bit group, the count of
its original bits. Possible counts are zero, one, or two, all of which fit in
two bits. Because each group has enough capacity, addition cannot carry into a
neighboring pair.

**Second stage: combine pairs into nibbles**

Mask `0x33333333` repeats binary `0011`, selecting the lower two-bit count from
each 4-bit nibble. The shifted expression moves the upper two-bit count down by
two. Adding them gives the number of original set bits in each 4-bit group.

That count ranges from zero through four and fits within the nibble. The mask
again prevents data from adjacent groups from mixing.

**Third stage: combine nibbles into bytes**

`0x0F0F0F0F` selects the low nibble of each byte, while shifting right by four
moves the high-nibble count into the same local position. Their sum is each
byte's population count, from zero through eight.

At this point, the integer conceptually contains four independent byte counts.
It no longer represents the original bit pattern, but it preserves exactly the
information needed for the final total.

**Fourth and fifth stages: reach one total**

Mask `0x00FF00FF` and a shift by eight combine neighboring byte counts into two
16-bit counts. Mask `0x0000FFFF` and a shift by sixteen then combine those two
halves. The final value of `n` is an ordinary integer between zero and 32 equal
to the number of original set bits.

No final mask is needed beyond the last expression because both operands place
their counts in the low 16-bit region, and the maximum possible sum 32 fits
comfortably there.

**Why the staged invariant proves the answer**

Initially every one-bit group trivially contains its own set-bit count: either
zero or one. Assume groups of width $g$ each contain the correct count for their
original positions. The next expression masks one adjacent group, shifts the
other into alignment, and adds the two counts. It therefore creates the correct
count for the combined width $2g$.

Applying this reasoning at widths 1, 2, 4, 8, and 16 shows that the final
32-bit group contains the count across all input positions. Mask patterns keep
groups independent, and each group's numeric capacity prevents cross-group
carry. This establishes exactness without enumerating individual bits in code.

**Trace a small byte conceptually**

For byte `10110010`, adjacent pair counts are `01,10,01,01` when read as local
numeric groups. Combining those pairs creates nibble counts two and two.
Combining the nibbles produces four, matching the four visible 1-bits. The
32-bit source performs the same hierarchy over four bytes at once.

**Fixed-width input keeps Python behavior controlled**

The Reference supplies a positive value no larger than $2^{31}-1$. Right shift
therefore fills with zeros, and every hexadecimal mask confines operations to
the intended low 32 positions. Negative arbitrary-precision Python integers
would require an initial `& 0xffffffff` to define a finite raw bit pattern.

**Understand the inactive alternatives**

`Solution2` precomputes a 256-element byte-popcount table in every instance.
It repeatedly looks up `n & 0xff` and shifts by eight. This directly addresses
the repeated-call follow-up, although a shared class-level table could avoid
rebuilding it for each object.

`Solution3` uses the `n &= n - 1` technique from the optimal variant, performing
one iteration per set bit. `Solution4` formats the positive integer as binary
text and counts `'1'` characters, which is concise but allocates a string.
These classes are not selected when the platform instantiates `Solution`.

**Interpret the source complexity comment**

The comment notes that Python shifts on arbitrary-size integers take time
proportional to represented word length. That is important for unbounded
inputs. Under this problem's fixed 32-bit range, however, the operand size and
all five stages are bounded constants, so the manifest's $O(1)$ classification
is appropriate.

## Complexity detail

The selected algorithm performs five fixed mask, shift, and addition stages.
With 32-bit bounded input, time is $O(1)$. For an arbitrary $w$-bit integer, a
similar parallel reduction would use $O(\log w)$ stages and each big-integer
operation would have a width-dependent cost.

Only the evolving integer `n` and constant masks are used, so auxiliary space
is $O(1)$ under the fixed-width model. The inactive byte table contains 256
entries, which is also constant for 32-bit inputs but has a larger fixed
footprint.

## Alternatives and edge cases

- **Kernighan bit clearing:** `Solution3` and the optimal variant perform one iteration per set bit and are easier to remember.
- **Byte lookup:** `Solution2` uses four conceptual chunks and is attractive for repeated calls.
- **Hardware or built-in popcount:** Often the fastest practical choice when the language exposes it.
- **Loop over 32 masks:** Fixed, beginner-friendly, and avoids the denser SWAR constants.
- **Zero:** Every group count remains zero; the final result is zero even though input is specified positive.
- **Power of two:** Parallel reduction ultimately produces one.
- **Maximum positive signed value:** Its 31 low bits are set, so the result is 31.
- **No cross-group carry:** Correctness relies on each partial count fitting in its allocated group width.
- **Negative input:** Outside the contract; mask to 32 bits before using Python shifts.
- **Different word width:** The constants and number of combination stages must be redesigned.
