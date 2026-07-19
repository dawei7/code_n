## General
**Convert the problem to a nonnegative exponent once**

When `n` is negative, replace the base by its reciprocal and work with `-n`, using the identity $x^{n} = (1/x)^{-n}$. This reduces every remaining step to a nonnegative exponent and avoids mixing sign logic into the bit loop. Python integers safely represent $-(-2^{31})$; a fixed-width implementation must widen or otherwise safely negate the exponent first.

**Consume one binary exponent bit per iteration**

Maintain `result`, `base`, and the remaining exponent. If the exponent's low bit is `1`, multiply `result` by the current base power. Then square `base` and shift the exponent right. Squaring changes the represented factor from $x^{2^k}$ to $x^{2^{k+1}}$, while the shift exposes the next binary coefficient.

**The accumulated and unprocessed factors retain the same product**

At every iteration, `result * base ^ exponent` equals the requested normalized power. Multiplying `result` by `base` removes an odd factor; squaring the base while halving an even exponent preserves the product. When the exponent becomes zero, the invariant leaves `result` as the answer.

**Trace set bits rather than ten multiplications**

For $2^{10}$, binary `10` is `1010`. The method squares the base through `2`, `4`, `16`, and `256`, multiplying only for the set bits. The accumulated result becomes $4 \cdot 256 = 1024$ in four iterations rather than ten.

**Each exponent bit preserves the remaining power**

Maintain `result * base ^ exponent = x ^ abs(n)` after any negative-exponent normalization. For an odd exponent, multiplying `result` by `base` accounts for its low set bit. Squaring `base` while halving the exponent then uses `base ** ((2k)) = (base ** 2) ** k`, preserving the same total power for both odd and even cases.

When the exponent reaches zero, the remaining factor is one and `result` equals $x ^ | n |$. If the original exponent was negative, replacing the base by its reciprocal at the start makes that same invariant evaluate $x^{n}$ directly.

## Complexity detail
The exponent is halved each iteration, so the loop runs $O(\log |n|)$ times. It keeps only a constant number of numeric variables, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Multiply $| n |$ times:** is correct for modest exponents but takes $O(|n|)$ time.
- **Recursive exponentiation by squaring:** has the same time complexity but consumes $O(\log |n|)$ call-stack space.
- **Built-in power:** hides the algorithm the exercise asks to implement.
- Exponent zero returns the multiplicative identity `1`, including when no loop iteration runs.
- Floating-point rounding, overflow, and underflow follow the language's numeric semantics; exponentiation by squaring reduces operation count but cannot make floating arithmetic exact.
