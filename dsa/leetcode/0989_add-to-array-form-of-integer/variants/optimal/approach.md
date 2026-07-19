## General
**Use `k` as the initial carry:** Start at the final digit of `num`. Add that digit to the current carry, append `total % 10` to a reversed result, and update the carry with `total // 10`. Move one position left and repeat.

**Continue until both sources are exhausted:** The loop runs while an input digit remains or the carry is nonzero. Once `k` has been reduced to zero, the same operation copies remaining digits unless a previous addition still propagates a carry. If the carry remains after the most significant input digit, its decimal digits are emitted by further iterations.

At each step, the appended digit is the correct digit for the current decimal place because division by ten separates that place's remainder from everything that belongs farther left. Reversing the collected least-significant-first digits yields the exact conventional array-form of the sum.

## Complexity detail
The loop processes at most $L+1$ decimal places, so time is $O(L)$. The returned digits use $O(L)$ space; counters and carry use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Convert the full array to an integer:** Repeatedly growing an arbitrary-precision integer performs increasingly expensive arithmetic and is unavailable in fixed-width languages for up to $10^4$ digits.
- **Convert through a decimal string:** Standard integer parsers may reject or overflow such a long value and obscure the simple digit-wise addition.
- **Carry through every digit:** Inputs made entirely of nines can add one extra leading digit.
- **Zero array-form:** `num = [0]` is valid and produces the ordinary digits of `k`.
- **`k` has more digits:** After all input digits are consumed, remaining carry digits are emitted normally.
