## General
This is long division with one extra observation: the remainder is the complete state of the fractional computation. If the same nonzero remainder appears twice, every digit from that point onward must repeat in the same order.

Handle the sign before doing any division. Zero returns `"0"` immediately; otherwise prepend `-` exactly when the operands have opposite signs, then work with absolute values. Integer division produces the whole-number part, and the remainder determines whether a decimal point is needed. A zero remainder means the fraction was an exact integer.

For the fractional part, record each remainder's output position **before** using it to generate a digit. Then repeat:

1. Multiply the remainder by ten.
2. Append the quotient digit from division by the denominator.
3. Replace the remainder with the new modulus.

If the remainder becomes zero, the decimal terminates. If it has already been recorded, insert `(` at that remainder's first output position and append `)` at the end.

Consider $4 / 333$. The initial remainder is `4`. Long division produces a `0` and remainder `40`, then `1` and remainder `67`, then `2` and remainder `4`. Because remainder `4` has returned, the future computation is identical to the state before the first fractional digit, so the result is `0.(012)`. Recording output positions rather than merely a set of remainders tells us exactly where the opening parenthesis belongs.

There can be at most `abs(denominator) - 1` distinct nonzero remainders. Therefore long division must eventually reach remainder zero or revisit an earlier remainder; it cannot continue forever without revealing the terminating or repeating structure.

At every step, ordinary integer long division emits the next exact decimal digit and carries the exact remainder. A zero remainder proves that no fractional value remains. For a nonzero remainder, the denominator and that remainder uniquely determine every future digit. Repeating a remainder therefore starts a recurring suffix, and its first recorded position is the earliest start of that cycle. Since all preceding digits were generated exactly by long division, adding parentheses around precisely this suffix produces the required exact representation.

## Complexity detail
Let `k` be the number of fractional digits generated before termination or the first repeated remainder. Each state is processed once, for $O(k)$ time. The remainder-position map and output buffer use $O(k)$ space. Since there are fewer than `abs(denominator)` nonzero remainder states, `k` is bounded accordingly.

## Alternatives and edge cases
- Floating-point conversion is unsuitable because rounding loses exactness and does not identify a recurring cycle reliably.
- Reducing the fraction can shorten the arithmetic, but cycle detection is still required unless the reduced denominator contains only factors `2` and `5`.
- Zero must never be formatted as negative, even if the denominator is negative.
- The quotient may be an exact integer, have magnitude below one, or have zeroes at the beginning of its recurring block.
- In fixed-width languages, convert operands to a wider type before taking absolute values so the minimum signed integer does not overflow.
