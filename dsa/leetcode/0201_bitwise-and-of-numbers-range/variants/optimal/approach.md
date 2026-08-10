## General

**Find which bit positions can survive a whole range**

Bitwise AND keeps a 1 at a position only when every number in the inclusive
range has a 1 there. If even one number has zero at that position, the final
bit is zero.

Binary representations of `left` and `right` share some high-order prefix. At
their highest differing position, `left` has 0 and `right` has 1. The range
crosses that binary boundary, so that position and every less significant
position vary somewhere across the interval. None of those suffix positions
can be guaranteed 1. Only the common high-order prefix can survive, followed by
zeros.

**Clear the right endpoint's least significant 1-bit**

The update `right &= right - 1` is Brian Kernighan's bit-clearing identity.
Subtracting one changes the least significant 1-bit of `right` to zero and
changes lower trailing zeros to ones. AND with the original clears the chosen
1 and also clears those newly introduced lower ones, while preserving every
higher bit.

For example, `1101000 - 1` is `1100111`, and their AND is `1100000`. Exactly
the rightmost set bit of the original value disappears.

**Continue while the candidate is above `left`**

The current `right` is always the original upper endpoint with some low 1-bits
cleared. While it remains greater than `left`, it still contains a set bit in
the suffix where the range's binary values vary. Such a bit cannot survive the
AND of every range value, so clearing it is safe.

The loop stops once the transformed value is less than or equal to `left`. It
need not become exactly equal. For `[5,6]`, binary endpoints are `101` and
`110`; clearing 6's lowest 1 gives `100`, which is 4, below 5. That value is
also `5 & 6`.

**Why the loop cannot clear a common-prefix bit**

Imagine all lower varying 1-bits have been removed from the original right
endpoint. The remaining value consists of the endpoints' common prefix followed
by zeros. That value is no greater than `left`, whose prefix is the same and
whose lower suffix is nonnegative. The loop condition is now false.

Therefore the algorithm stops before attempting to clear any 1-bit in the
common prefix. It removes exactly the upper endpoint's set bits that lie in the
unstable suffix.

**Trace `[5,7]`**

The binary interval is `101`, `110`, `111`. Start with `right = 111`.

- Since 5 is less than 7, clear the least significant 1: `111 & 110 = 110`.
- Since 5 is still less than 6, clear the next least significant 1:
  `110 & 101 = 100`.
- Now transformed `right = 4` is not greater than `left = 5`, so stop.

The returned `100` is 4. Direct AND confirms `101 & 110 & 111 = 100`.

**Why the returned value is exact**

Every bit cleared by the loop lies at or below the highest position where the
endpoints differ. The interval contains values with both zero and one in those
varying positions, so the true range AND must clear them. The loop never clears
the stable common prefix, whose bit values are identical for every number in
the interval.

At termination, all remaining lower positions are zero and all remaining high
positions are precisely that common prefix. This is exactly the only pattern
that can survive AND across the complete range.

**The interval width does not drive the loop**

A brute-force solution would AND every integer and could require more than two
billion operations. This method performs one iteration only when it removes a
set bit from the upper endpoint. Large numeric intervals are therefore handled
in at most the integer word width, independent of how many values the interval
contains.

**Boundary behavior**

When `left == right`, the loop does nothing and returns that sole range value.
When `left == 0`, any range result must be zero because zero participates in
the AND; the loop eventually clears `right` to zero. The expression
`right - 1` is never evaluated with `right == 0` while the condition is true,
because nonnegative `left < right` then implies positive `right`.

The inputs are nonnegative, so Python's unbounded signed-integer right-shift
issues are irrelevant and bit clearing monotonically decreases the value.

**Manifest wording versus exact code**

The manifest summary describes shifting both endpoints right to isolate their
common prefix, then shifting it back. That is a valid editorial approach, but
the exact selected solution instead clears set bits from `right`. Both derive
the same common-prefix result; this document follows the actual source.

## Complexity detail

Let $b$ be the bit width of `right`, so $b = O(\log(right+1))$. Each iteration
clears one set bit, and no more than $b$ bits can be cleared. Time is therefore
$O(\log right)$ as recorded by the manifest, with a tighter bound based on the
number of removable suffix 1-bits.

For the fixed 31-bit nonnegative domain, the loop count is bounded by a constant,
so the editorial can also call it $O(1)$. Only the two endpoints and temporary
integer results are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Common-prefix shifts:** Shift both endpoints right until equal, count shifts, then restore the prefix with a left shift.
- **Brute-force range AND:** Correct but proportional to `right - left + 1`, which is infeasible for wide intervals.
- **Highest-difference mask:** Find the most significant differing endpoint bit and clear that bit and everything below in one calculation.
- **Equal endpoints:** Return the endpoint unchanged.
- **Range beginning at zero:** Return zero after all upper set bits are cleared.
- **Crossing a power of two:** The high prefix may become zero, making the whole result zero.
- **Narrow range:** Only a few suffix bits may need clearing.
- **Maximum endpoint:** Still at most 31 clearing iterations under the contract.
- **Nonnegative guarantee:** Ensures monotonic finite bit-clearing behavior.
- **Common-prefix bit:** The stopping condition prevents it from being cleared.
