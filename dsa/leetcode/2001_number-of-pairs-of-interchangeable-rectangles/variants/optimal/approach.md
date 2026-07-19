## General
**Represent each ratio exactly.** For dimensions `(width, height)`, compute $g=\gcd(\textit{width},\textit{height})$ and use `(width // g, height // g)` as its canonical key. Two positive fractions have the same reduced numerator and denominator exactly when their ratios are equal, avoiding floating-point rounding and integer-division mistakes.

**Count partners as each rectangle arrives.** Maintain a frequency map from reduced ratio keys to the number of earlier rectangles with that key. If the current key has appeared $c$ times, the current index forms exactly $c$ new pairs—one with each earlier matching index. Add $c$ to the answer, then increment the frequency.

Every valid pair is counted once, when its larger index is processed. No invalid pair is counted because different exact reduced ratios receive different keys. This incremental count is equivalent to summing $\binom{c}{2}$ for each final ratio-group size $c$ without requiring a second pass.

## Complexity detail
Euclid's algorithm computes each greatest common divisor in $O(\log M)$ time, so processing all rectangles takes $O(N\log M)$ time. At most $N$ distinct reduced ratios are stored, giving $O(N)$ space.

## Alternatives and edge cases
- **Compare every pair:** Cross multiplication gives an exact equality test but examines $O(N^2)$ pairs.
- **Use floating-point division as the key:** This is concise but makes correctness depend on binary rounding; reduced integer pairs are exact.
- **Use integer division only:** Ratios such as $3/2$ and $4/3$ have the same truncated quotient but are not interchangeable.
- A single rectangle creates no pair.
- Duplicate rectangles at different indices each contribute independently.
- Large groups can produce more than 32-bit many pairs, so languages with fixed-width integers need a 64-bit accumulator.
