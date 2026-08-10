## General

**Reverse progressively smaller blocks**

The selected competitive `Solution` does not inspect individual bits in a
loop. It applies a fixed five-stage permutation. First it swaps the two 16-bit
halves, then swaps 8-bit blocks inside each half, then 4-bit blocks, 2-bit
blocks, and finally adjacent 1-bit positions.

After the last stage, every original position has crossed every boundary needed
to reach its mirror position. This is a divide-and-conquer reversal network:
each stage fixes one more level of the bit-position hierarchy.

**Swap the 16-bit halves**

`(n >> 16)` moves the original high half into the low 16 positions.
`(n << 16)` moves the original low half into positions 16 through 31. OR merges
the two pieces.

In a fixed-width 32-bit language, bits shifted past position 31 are discarded
automatically. Python integers have arbitrary precision, so `n << 16` also
temporarily preserves original high-half bits above position 31. The next stage
uses masks confined to the low 32 positions, discarding those extra bits before
they can affect the result. An explicit `& 0xffffffff` after the first line
would make the fixed-width intent more obvious.

**Swap neighboring bytes**

Mask `0xff00ff00` selects the upper byte of each 16-bit region. Shifting that
selection right by eight moves those bytes into the lower byte positions.
Mask `0x00ff00ff` selects the lower bytes, and shifting left by eight moves
them upward. OR combines the nonoverlapping destinations.

At this point, the order of all four bytes is reversed, but bits inside each
byte remain in their original order.

**Swap nibbles, pairs, and individual bits**

The next line uses `0xf0f0f0f0` and `0x0f0f0f0f` to exchange the high and low
4-bit nibbles within every byte. The following line uses alternating two-bit
groups: hexadecimal `c` is binary `1100`, and hexadecimal `3` is `0011`, so
shifting by two exchanges those groups.

The final line uses `0xaaaaaaaa` and `0x55555555`. Their binary forms alternate
`10` and `01`, selecting odd-positioned and even-positioned bits. Shifting the
selected sets by one exchanges every adjacent pair. Nothing remains grouped,
so the complete 32-bit order is reversed.

**Why masks are required at every stage**

A plain shift would move a desired block but leave unrelated bits in the same
integer. The masks isolate exactly the blocks moving in one direction. The two
masked pieces have disjoint destination positions, so bitwise OR combines them
without collision or carry.

Each source bit appears in exactly one of the complementary masks at a stage.
It is moved by the appropriate distance and never discarded within the low
32-bit domain. Therefore every stage is a permutation of positions, not a
lossy transformation.

**See the hierarchy on a small scale**

For an eight-bit word, the analogous process would swap 4-bit halves, then
2-bit pairs, then adjacent bits. A bit's destination address is obtained by
reversing the decisions “which half, which pair, which side” made at each
level. The five 32-bit stages perform exactly this address reversal across five
binary index bits, mapping position $i$ to $31-i$.

**Why the final integer matches the contract**

The 32 source positions are permuted bijectively: each stage maps every selected
position to one unique partner position. Composing the stages maps every bit to
its mirror and covers every destination once. Zero positions move just like
one positions, so leading zeros are handled even though they have no visible
integer digits.

The Reference's nonnegative input makes right shifts logical in effect. Its
even-input guarantee means original bit zero is clear and the final high bit is
clear, though the network itself does not depend on evenness.

**Understand the inactive `Solution2`**

The file also defines `Solution2`, but the normal entry point is the first class
named `Solution`. `Solution2` is a straightforward bit-by-bit alternative. It
repeats 32 times, shifts the result left, copies `n & 1` into the new low
position, and shifts `n` right.

That construction reads source bits from low to high while appending them to
the result from high significance over time. It is correct under the same
nonnegative 32-bit contract, but it is not invoked when the selected `Solution`
class is used.

**Repeated-call follow-up**

The mask network already has a fixed small operation count and no data-dependent
branches. Another response to repeated calls is a precomputed table containing
the reversal of all 256 possible bytes. Each input can then be split into four
bytes, looked up, and reassembled in reverse byte order. The table has constant
size under a fixed-width analysis.

## Complexity detail

The primary method always executes five mask-and-shift assignments regardless
of the input value. Under a fixed 32-bit contract, time is $O(1)$. It performs
no loop and has no input-dependent early or late path.

It stores only the current integer and constant literal masks, so auxiliary
space is $O(1)$. Python may temporarily create an integer wider than 32 bits
after the first left shift, but its width is still bounded by a constant and is
trimmed logically by the following masks.

## Alternatives and edge cases

- **Bit-by-bit loop:** Inactive `Solution2` uses 32 simple iterations and is often easier to derive.
- **Byte memoization:** Cache reversals for 0 through 255 and process four chunks, directly addressing frequent calls.
- **Explicit first-stage mask:** Add `& 0xffffffff` to document Python's fixed-width truncation even though the next masks remove high bits.
- **Two-bit encoding tables:** Smaller chunks reduce table size but require more lookups and assembly steps.
- **Zero:** Every stage preserves zero.
- **Leading zero positions:** Masks permute them into trailing positions even though they are not printed.
- **Even input:** Ensures the reversed high position is zero; no conditional handling is needed.
- **Odd unsigned input:** The network can reverse it too, but the result may use bit 31 and exceed this Reference's signed-positive range.
- **Negative Python input:** Outside the contract; first mask to 32 bits to avoid arithmetic right-shift sign extension.
- **Fixed width:** These exact masks are specific to 32 positions and must change for another word size.
