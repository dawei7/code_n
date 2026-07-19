## General
**Reverse the operations to expose forced choices**

Imagine reducing the target back to all zeros. If any current entry is odd, a global division by two is impossible because it would not preserve integer values. That odd entry must first be reduced by one, reversing a single-entry increment. Once every entry is even, dividing the whole array by two reverses one global doubling and is always at least as useful as further decrements.

Each time an entry is odd during this process, its lowest binary bit is one. Removing that one and later dividing shifts the next bit into place. Consequently, a value requires exactly one individual increment for each set bit in its binary representation. These calls cannot be shared between positions, so their minimum total is the sum of all population counts.

**Share every useful doubling**

A target whose highest set bit is at position $k$ cannot be built with fewer than $k$ global doublings: an increment creates a unit, and each doubling can move its contribution only one binary position left. Conversely, performing exactly the largest such $k$ across all entries supplies enough shared doubling stages for every value. Entries with fewer bits simply receive no increments during the earlier stages.

The minimum is therefore the sum of all set-bit counts plus $B-1$ when $B>0$. Scan the array once, accumulating population counts and the maximum bit length. If every value is zero, both contributions are zero.

## Complexity detail
Counting the bits of one value takes $O(B)$ in a language-independent bit scan, so all $N$ values take $O(NB)$ time. Since $B \le 30$ under the source contract, this is also linear in $N$ for legal inputs. The implementation stores only two running totals, giving $O(1)$ auxiliary space.

The three benchmark tiers scale $N$ while keeping legal 30-bit values. They distinguish the one-pass computation from a correct implementation that redundantly recomputes prefix maxima and therefore performs quadratic work.

## Alternatives and edge cases
- **Explicit reverse simulation:** repeatedly decrement all odd entries and halve the array when it becomes even. This mirrors the proof and has the same $O(NB)$ bound, but revisits the full array for each bit layer.
- **Binary-string counting:** convert each value to base two and count `1` characters. It is correct but allocates temporary strings that direct bit operations avoid.
- **Forward construction:** process bit positions from most significant to least significant, doubling between levels and incrementing positions whose next bit is one. This constructs an optimal sequence but stores more operational detail than the count requires.
- **All-zero target:** no increment or doubling is needed, so the answer is zero rather than a negative doubling count.
- **Single element:** the formula reduces to the set-bit count plus its highest set-bit position.
- **Repeated values:** increments remain position-specific even when values match, while the doubling calls are shared.
- **Mixed bit lengths:** only the largest bit length determines the number of doublings; shorter values need no padding operations.
- **Maximum values:** `1000000000` has a legal 30-bit representation, so all counting remains within the stated bound.
