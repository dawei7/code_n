## General

**Count complete bit lengths from their free leading halves.** A positive palindrome of bit length $L$ is uniquely determined by its first

$$
h=\left\lceil\frac{L}{2}\right\rceil
$$

bits. The first of those bits must be one, while the remaining $h-1$ bits are arbitrary. Therefore exactly

$$
2^{h-1}=2^{\left\lfloor(L-1)/2\right\rfloor}
$$

positive palindromes have length $L$. Add this quantity for every length shorter than the bit length of `n`, and add one separately for zero.

**Resolve the current length with one mirrored prefix.** Let $P$ be the integer represented by the first $h$ bits of `n`. The smallest valid leading half is $2^{h-1}$. Every prefix from that smallest value through $P-1$ produces a same-length palindrome strictly below `n`, contributing $P-2^{h-1}$ values.

Only prefix $P$ remains undecided. Build its palindrome by appending the reversed prefix, omitting the middle prefix bit when $L$ is odd. Include this one additional value exactly when the result is at most `n`. Prefixes larger than $P$ necessarily produce larger numbers, so no other candidate can qualify.

## Complexity detail

There are $O(\log n)$ possible bit lengths, and mirroring the boundary prefix processes at most $O(\log n)$ bits. The total time is $O(\log n)$. The implementation stores a constant number of integer counters and uses $O(1)$ auxiliary machine words under the problem's fixed 50-bit bound.

The benchmark uses its `size` as the numeric upper bound $n$. The accepted method grows with its bit length. A calibrated correct alternative enumerates every integer through $n$ and tests its binary representation, which returns the same counts but grows essentially linearly in the numeric bound.

## Alternatives and edge cases

- **Enumerate every integer:** Converting and checking each binary representation is straightforward but requires work proportional to the numeric bound.
- **Generate every palindrome:** Mirroring all possible leading halves avoids non-palindromes but still produces $\Theta(\sqrt n)$ candidates instead of counting full lengths directly.
- **Zero:** It must be counted separately because the positive-length formula assumes a leading one.
- **Exact palindromic bound:** The mirrored current prefix is included when it equals `n` because the interval is inclusive.
- **Boundary below the mirror:** If the mirrored prefix exceeds `n`, no palindrome using that prefix is counted.
- **Odd bit length:** Do not duplicate the central bit while mirroring the leading half.
- **No leading zeros:** Requiring the first prefix bit to be one enforces the canonical binary representation.
